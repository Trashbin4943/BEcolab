from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationLoginTest(APITestCase):
    """
    회원가입 및 로그인 기능 테스트 케이스
    """

    def setUp(self):
        """
        테스트 케이스 실행 전에 공통적으로 필요한 데이터를 설정합니다.
        """
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        
        # 회원가입에 사용할 데이터
        self.user_data = {
            'email': 'testuser@example.com',
            'password': 'somepassword123',
            'nickname': 'testnickname'
        }
        
        # 미리 사용자 한 명을 생성해 둡니다. (로그인 테스트용)
        self.user = User.objects.create_user(
            email='loginuser@example.com',
            password='loginpassword123',
            nickname='loginnickname'
        )

    def test_user_registration_success(self):
        """
        회원가입 성공 테스트
        """
        print("회원가입 성공 테스트 시작")
        # 클라이언트로 user_data를 POST 방식으로 전송 (API 요청)
        response = self.client.post(self.register_url, self.user_data, format='json')
        
        # 1. 응답 상태 코드가 201 CREATED 인지 확인
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # 2. 실제로 데이터베이스에 User가 생성되었는지 확인
        self.assertTrue(User.objects.filter(email=self.user_data['email']).exists())
        print("회원가입 성공 테스트 완료")

    def test_user_registration_fail_email_exists(self):
        """
        회원가입 실패 테스트 (이미 존재하는 이메일)
        """
        print("회원가입 실패 테스트 (이메일 중복) 시작")
        # 이미 존재하는 이메일로 가입 시도
        existing_user_data = {
            'email': 'loginuser@example.com', # setUp에서 생성한 사용자의 이메일
            'password': 'newpassword123',
            'nickname': 'newnickname'
        }
        response = self.client.post(self.register_url, existing_user_data, format='json')
        
        # 1. 응답 상태 코드가 400 BAD REQUEST 인지 확인
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("회원가입 실패 테스트 (이메일 중복) 완료")

    def test_user_login_success(self):
        """
        로그인 성공 테스트
        """
        print("로그인 성공 테스트 시작")
        login_data = {
            'email': 'loginuser@example.com',
            'password': 'loginpassword123'
        }
        response = self.client.post(self.login_url, login_data, format='json')
        
        # 1. 응답 상태 코드가 200 OK 인지 확인
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # 2. 응답 데이터(JSON)에 'access' 토큰과 'refresh' 토큰이 포함되어 있는지 확인
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        print("로그인 성공 테스트 완료")

    def test_user_login_fail_wrong_password(self):
        """
        로그인 실패 테스트 (잘못된 비밀번호)
        """
        print("로그인 실패 테스트 (비밀번호 오류) 시작")
        login_data = {
            'email': 'loginuser@example.com',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.login_url, login_data, format='json')
        
        # 1. 응답 상태 코드가 401 UNAUTHORIZED 인지 확인
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        print("로그인 실패 테스트 (비밀번호 오류) 완료")
