# Spartamarket - DRF
spartamarket DRF는 Django REST Framework 을 사용하여 유저관리와 제품관리를 할수 있는 어플리케이션 입니다.

### 4조 박혜진


## 모델
### 1. 유저와 프로필 :
* - User : 장고의 내장 모델
  - Profile : 닉네임 생일 성별등을 사용자 정보에 추가하는 모델
### 2.제품 :
* - Product : 이름 가격 수량등의 속성을 가진 제품을 나타내는 모델

## API
### 사용자 및 프로필:
* 회원가입: POST /signup/ - 새로운 사용자를 등록하고 관련 프로필을 생성합니다.
* 로그인: POST /signin/ - 인증을 받고 API 접근을 위한 JWT를 받습니다.
* 프로필 조회: GET /profiles/{username}/ - 사용자 이름을 기준으로 프로필 정보를 검색합니다.
* [
* 회원가입 POST : http://127.0.0.1:8000/api/v1/accounts/profiles/
* 로그인 POST: http://127.0.0.1:8000/api/v1/accounts/signin/
* 프로필리스트 GET: http://127.0.0.1:8000/api/v1/accounts/profiles/
* 프로필조회 GET: http://127.0.0.1:8000/api/v1/accounts/profiles/scottjennifer/
* ]

### 제품:
* 제품 목록 조회: GET /products/ - 모든 제품의 목록을 조회합니다 (선택적 페이징 가능).
* 제품 생성: POST /products/ - 시스템에 새 제품을 추가합니다.
* 제품 상세 조회: GET /products/{pk}/ - 특정 제품의 상세 정보를 조회합니다.
* 제품 수정: PUT /products/{pk}/ - 특정 제품의 상세 정보를 수정합니다.
* 제품 삭제: DELETE /products/{pk}/ - 시스템에서 제품을 삭제합니다.
* [
* 상품등록 POST : http://127.0.0.1:8000/api/v1/products/ 
* 상품목록 조회 GET : http://127.0.0.1:8000/api/v1/products/ 
* 상품수정 PUT : http://127.0.0.1:8000/api/v1/products/5/
* 상품삭제 DELETE :http://127.0.0.1:8000/api/v1/products/5/
* ]

## 권한
* JWT 인증


## 설치및 설정방법
* git clone
* 새터미널~~
* python -m venv venv
* source venv/Scripts/activate
* pip install django==4.2
* pip install djangorestframework
* pip install django-extentions
* pip freeze > requirments.txt

* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver

* 로그인이 안될때는 슈퍼유저 생성후 보기  python manage.py createsuperuser

### TMI
- 서버상으로는 회원가입되는데 포스트맨에서는 회원가입 send 하면 에러뜸
- 캡쳐본 올리고 싶은데 어떻게 올리는지 모르겠고 시간도 없음
- 페이지네이션 하다가 망했음


