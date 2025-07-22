# BEcolab 🎬

영화 정보와 리뷰를 제공하는 웹 애플리케이션입니다.

## 📋 프로젝트 개요

BEcolab은 사용자들이 영화 정보를 조회하고 리뷰를 작성할 수 있는 플랫폼입니다. Django REST Framework를 기반으로 구축된 백엔드 API와 React 프론트엔드로 구성되어 있습니다.

## 👥 개발자

- **조현한(백엔드)**
- **황준호(백엔드)**
- **최선지(프론트엔드)**
- **박윤정(프론트엔드)**

## 🚀 주요 기능

### 🎥 영화 관리
- 영화 정보 조회 (한글/영문 제목, 포스터, 장르, 상영시간, 개봉일, 줄거리, 평점)
- 감독 및 배우 정보 관리
- 영화 검색 및 필터링

### 👤 사용자 관리
- 회원가입 및 로그인 (이메일 기반)
- JWT 토큰 기반 인증
- 사용자 프로필 관리

### 💬 리뷰 시스템
- 영화별 댓글 작성
- 별점 평가 시스템
- 사용자별 리뷰 관리

## 🛠 기술 스택

### Backend
- **Django 5.2.4** - 웹 프레임워크
- **Django REST Framework** - API 서버
- **MySQL** - 데이터베이스
- **JWT** - 인증 시스템
- **drf-yasg** - API 문서화 (Swagger)

### Frontend
- **React** - UI 라이브러리

### DevOps & Deployment
- **Docker & Docker Compose** - 컨테이너화
- **Nginx** - 웹 서버 및 리버스 프록시
- **Gunicorn** - WSGI 서버
- **Let's Encrypt (Certbot)** - SSL 인증서

### 주요 라이브러리
```
Django==5.2.4
djangorestframework==3.16.0
djangorestframework-simplejwt==5.5.0
dj-rest-auth==7.0.1
django-allauth==65.10.0
django-cors-headers==4.7.0
drf-yasg==1.21.10
mysqlclient==2.2.7
gunicorn==23.0.0
```

## 📁 프로젝트 구조

```
BEcolab/
├── bepjt/                    # Django 프로젝트 설정
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── movies/                   # 영화 앱
│   ├── models.py            # Movie, Director, Actor, Comment 모델
│   ├── serializers.py       # API 시리얼라이저
│   ├── views.py             # API 뷰
│   └── urls.py
├── users/                    # 사용자 앱
│   ├── models.py            # 커스텀 User 모델
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── frontend/                 # React 프론트엔드
│   └── build/               # 빌드된 정적 파일
├── static/                   # Django 정적 파일
├── docker-compose.yml        # Docker 구성
├── Dockerfile
├── nginx.default.conf        # Nginx 설정
├── requirements.txt          # Python 의존성
└── manage.py
```

## 🏃‍♂️ 실행 방법

### 1. 저장소 클론
```bash
git clone https://github.com/Trashbin4943/BEcolab.git
cd BEcolab
```

### 2. 환경 변수 설정
```bash
# .env 파일 생성 (예시)
SECRET_KEY=your-secret-key
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=your-db-host
DB_PORT=3306
```

### 3-1. 로컬 개발 환경

#### Python 가상환경 설정
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

#### 데이터베이스 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 개발 서버 실행
```bash
python manage.py runserver
```

### 3-2. Docker를 이용한 실행

```bash
# Docker 이미지 빌드
docker build -t server .

# Docker Compose로 실행
docker-compose up -d
```

## 📚 API 문서

서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:

- **Swagger UI**: `http://localhost:8000/swagger/`
- **ReDoc**: `http://localhost:8000/redoc/`

## 🔗 주요 API 엔드포인트

### 인증
- `POST /auth/registration/` - 회원가입
- `POST /auth/login/` - 로그인
- `POST /auth/logout/` - 로그아웃

### 영화
- `GET /movies/` - 영화 목록 조회
- `GET /movies/{id}/` - 영화 상세 조회
- `POST /movies/{id}/comments/` - 댓글 작성
- `GET /movies/{id}/comments/` - 댓글 목록 조회

### 사용자
- `GET /users/profile/` - 프로필 조회
- `PUT /users/profile/` - 프로필 수정

## 🌐 배포 정보

- **도메인**: movielike.store, www.movielike.store
- **서버**: AWS EC2 (13.209.0.75)
- **SSL**: Let's Encrypt 인증서 적용

## 🗃 데이터베이스 모델

### User (사용자)
- 이메일 기반 인증
- 닉네임 시스템
- Django의 AbstractUser 확장

### Movie (영화)
- 한글/영문 제목
- 포스터, 장르, 상영시간, 개봉일
- 줄거리, 평점 정보

### Director (감독)
- 이름, 프로필 이미지

### Actor (배우)
- 이름, 캐릭터, 프로필 이미지

### Comment (댓글)
- 영화별 사용자 리뷰
- 별점 평가 시스템

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이센스

이 프로젝트는 MIT 라이센스를 따릅니다.

## 📞 문의

프로젝트에 대한 문의사항이 있으시면 이슈를 생성해주세요.

---

⭐ 이 프로젝트가 도움이 되었다면 스타를 눌러주세요!
