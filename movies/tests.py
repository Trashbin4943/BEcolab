from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Movie, Actor, Review

User = get_user_model()

class MovieReviewAPITest(APITestCase):
    """
    영화 및 리뷰 관련 API 테스트 케이스
    """

    @classmethod
    def setUpTestData(cls):
        """
        테스트 전체에서 한 번만 실행되는 설정입니다.
        변경되지 않는 데이터를 여기서 생성하면 효율적입니다.
        """
        print("setUpTestData: 테스트용 기본 데이터 생성 시작")
        # 테스트용 사용자 생성
        cls.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword123',
            nickname='testnickname'
        )

        # 테스트용 배우 생성
        cls.actor1 = Actor.objects.create(name='톰 행크스')
        cls.actor2 = Actor.objects.create(name='레오나르도 디카프리오')

        # 테스트용 영화 생성
        cls.movie1 = Movie.objects.create(
            title='포레스트 검프',
            genre='드라마',
            year=1994
        )
        cls.movie1.actors.add(cls.actor1)

        cls.movie2 = Movie.objects.create(
            title='인셉션',
            genre='SF',
            year=2010
        )
        cls.movie2.actors.add(cls.actor2)
        
        # 테스트용 리뷰 생성
        Review.objects.create(movie=cls.movie1, user=cls.user, content="인생 영화입니다.", rating=5)
        print("setUpTestData: 테스트용 기본 데이터 생성 완료")


    def setUp(self):
        """
        각 테스트 케이스 실행 전에 호출됩니다.
        API 요청 시 인증을 위해 클라이언트에 강제로 로그인시킵니다.
        """
        self.client.force_authenticate(user=self.user)
        
        # URL 리버스 네임 설정
        self.movie_list_url = reverse('movie-list')
        self.movie_detail_url = reverse('movie-detail', kwargs={'movie_id': self.movie1.id})
        self.movie_create_url = reverse('movie-create')
        self.review_create_url = reverse('review-create', kwargs={'movie_id': self.movie2.id})


    def test_movie_list_get(self):
        """
        영화 목록 조회 (GET) 테스트
        """
        print("영화 목록 조회 테스트 시작")
        response = self.client.get(self.movie_list_url)
        
        # 1. 응답 상태 코드가 200 OK 인지 확인
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # 2. 응답 데이터에 포함된 영화의 수가 2개인지 확인
        self.assertEqual(len(response.data), 2)
        
        # 3. 응답 데이터의 첫 번째 영화 제목이 '포레스트 검프'인지 확인
        self.assertEqual(response.data[0]['title'], '포레스트 검프')
        print("영화 목록 조회 테스트 완료")


    def test_movie_detail_get(self):
        """
        영화 상세 정보 조회 (GET) 테스트
        """
        print("영화 상세 조회 테스트 시작")
        response = self.client.get(self.movie_detail_url)
        
        # 1. 응답 상태 코드가 200 OK 인지 확인
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # 2. 응답 데이터의 영화 제목이 '포레스트 검프'인지 확인
        self.assertEqual(response.data['title'], '포레스트 검프')
        
        # 3. 영화에 달린 리뷰가 1개인지 확인
        self.assertEqual(len(response.data['reviews']), 1)
        
        # 4. 리뷰 내용이 올바른지 확인
        self.assertEqual(response.data['reviews'][0]['content'], "인생 영화입니다.")
        print("영화 상세 조회 테스트 완료")


    def test_movie_create_post(self):
        """
        영화 생성 (POST) 테스트
        """
        print("영화 생성 테스트 시작")
        new_movie_data = {
            "title": "새로운 영화",
            "genre": "코미디",
            "year": 2025,
            "actors": [self.actor1.id, self.actor2.id] # 배우는 ID 목록으로 전달
        }
        response = self.client.post(self.movie_create_url, new_movie_data, format='json')
        
        # 1. 응답 상태 코드가 201 CREATED 인지 확인
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # 2. 실제로 DB에 영화가 생성되었는지 확인
        self.assertTrue(Movie.objects.filter(title="새로운 영화").exists())
        
        # 3. 생성된 영화의 배우가 2명인지 확인
        new_movie = Movie.objects.get(title="새로운 영화")
        self.assertEqual(new_movie.actors.count(), 2)
        print("영화 생성 테스트 완료")


    def test_review_create_post(self):
        """
        리뷰 생성 (POST) 테스트
        """
        print("리뷰 생성 테스트 시작")
        review_data = {
            "content": "정말 재밌어요!",
            "rating": 4
        }
        response = self.client.post(self.review_create_url, review_data, format='json')
        
        # 1. 응답 상태 코드가 201 CREATED 인지 확인
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # 2. '인셉션' 영화의 리뷰 개수가 1개가 되었는지 확인
        movie2 = Movie.objects.get(id=self.movie2.id)
        self.assertEqual(movie2.reviews.count(), 1)
        
        # 3. 생성된 리뷰의 내용이 올바른지 확인
        self.assertEqual(movie2.reviews.first().content, "정말 재밌어요!")
        print("리뷰 생성 테스트 완료")
