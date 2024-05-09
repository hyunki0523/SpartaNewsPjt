
## * Description

   * ### Project name : Sparta News 
스파르타만의 뉴스 제공 서비스 구현

레퍼런스 : https://news.hada.io/

   * ### Project duration : 2024-05-03 ~ 2024-05-10


* ### Tech Explorers :

* | 황승환	👑  |	INFP |	https://github.com/hideoutoasis/spartamarket_DRF_by_HSH |	https://blog.naver.com/sunbook24 |
* | 김도연	member |	ISTJ | 병결		| https://sparkly-field-a92.notion.site/KDY-S-BLOG-d2eabf21b14b497eb4842a696977d06c?pvs=74 |
* | 이현기	member |	ISTP |	https://github.com/hyunki0523 |	https://blog.naver.com/dldl5040 |
* | 옹석현	member |	ISTP |	https://github.com/ongsh98 |	https://blog.naver.com/dhd9808	|

## * Environment & Tech stack
Window 환경에서 Pycham 사용. 

VisualStudio ,Python(3.10) , Django Framework (4.2.11) , Bootstrap 사용

Database : SQLite3 

API 기능 점검 : Postman 이용.

## * Prerequisite

Package|Version
-----------------

|----|----|----|----|

|alembic                        | 1.13.1 |
|asgiref                        | 3.7.2 |
|asttokens                      | 2.4.1 |
|beautifulsoup4                 | 4.12.3 |
|blinker                        | 1.7.0 |
|bs4                            | 0.0.2 |
|certifi                        | 2023.11.17 |
|cffi                           | 1.16.0 |
|charset-normalizer             | 3.3.2 |
|click                          | 8.1.7 |
|colorama                       | 0.4.6 |
|cryptography                   | 42.0.1 |
|decorator                      | 5.1.1 |
|Django                         | 4.2 |
|django-environ                 | 0.11.2 |
|django-extensions              | 3.2.3 |
|django-seed                    | 0.3.1 |
|djangorestframework            | 3.15.1 |
|djangorestframework-simplejwt  | 5.3.1 |
|et-xmlfile                     | 1.1.0 |
|exceptiongroup                 | 1.2.0 |
|executing                      | 2.0.1 |
|Faker                          | 24.4.0 |
|Flask                          | 3.0.2 |
|Flask-Migrate                  | 4.0.5 |
|Flask-SQLAlchemy               | 3.1.1 |
|greenlet                       | 3.0.3 |
|idna                           | 3.6 |
|ipython                        | 8.22.2 |
|itsdangerous                   | 2.1.2 |
|jedi                           | 0.19.1 |
|Jinja2                         | 3.1.3 |
|Mako                           | 1.3.2 |
|MarkupSafe                     | 2.1.5 |
|matplotlib-inline              | 0.1.6 |
|openpyxl                       | 3.1.2 |
|parso                          | 0.8.3 |
|pexpect                        | 4.9.0 |
|pillow                         | 10.2.0 |
|pip                            | 24.0 |
|prompt-toolkit                 | 3.0.43 |
|psycopg2                       | 2.9.9 |
|ptyprocess                     | 0.7.0 |
|pure-eval                      | 0.2.2 |
|pycparser                      | 2.21 |
|Pygments                       | 2.17.2 |
|PyJWT                          | 2.8.0 |
|pypng                          | 0.20220715.0 |
|python-dateutil                | 2.9.0.post0 |
|pytz                           | 2023.3.post1 |
|qrcode                         | 7.4.2 |
|requests                       | 2.31.0 |
|Send2Trash                     | 1.8.2 |
|setuptools                     | 65.5.0 |
|six                            | 1.16.0 |
|slack-bolt                     | 1.18.1 |
|slack_sdk                      | 3.26.2 |
|soupsieve                      | 2.5 |
|SQLAlchemy                     | 2.0.27 |
|sqlparse                       | 0.4.4 |
|stack-data                     | 0.6.3 |
|toposort                       | 1.10 |
|traitlets                      | 5.14.2 |
|typing_extensions              | 4.10.0 |
|tzdata                         | 2024.1 |
|urllib3                        | 2.1.0 |
|wcwidth                        | 0.2.13 |
|Werkzeug                       | 3.0.1 |


## * Roadmap

- [x] 회원기능 
    - [x] 회원가입, 로그인, 로그아웃
    - [x] 관리자계정
- [x] 프로필 페이지
  - [x] 찜 기능 
  - [x] 팔로우 기능 
  - [x] 개인프로필 설정(이미지, 태그)
- [x] 게시글 CRUD 
    - [x] 게시글 기능(제목, 내용)
    - [x] 정렬 기능( 좋아요순, 최신순 )
    - [x] 검색기능
    - [x] 로그인 권한을 바탕으로 CRUD 구현
    - [x] 댓글 CRUD

- TODO
- [ ] 배포

  
## * ERD<br/>
![SpartaNews ERD](https://github.com/hyunki0523/SpartaNewsPjt/assets/122522460/8c69f313-7ba6-463b-bd98-c0343999e0f4)
<br/><br/>

## * Use

별도의 템플릿 구현하지 않았으므로, postman 과 같은 API platform 을 통해 확인가능합니다.
구현한 기능은 크게 유저, 게시글 로 나눌수 있으며
유저의 경우
 회원가입, 로그인(JWT 사용, Token refresh 구현),
 로그아웃, 개인 프로필 페이지(가입할때 입력한 정보 확인가능)
게시글의 경우
 기본적으로 게시글을 목록형태로 확인가능하고 , 검색과 정렬 기능(좋아요 순, 최신 순)을 지원합니다.
 로그인을 한 경우 생성이 가능하고, 수정 및 삭제의 경우 작성자와 동일한 경우만 가능합니다.
 댓글의 CRUD 기능을 지원합니다.

### *로그인 기능

![1](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/268de151-1867-4bba-a4c0-058408082cb9)

### *토큰리프레시

![2](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/0f2a2bcb-f4e8-475f-8ddf-a158e08a54f0)
![2-1](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/2fc1968d-7b9c-4324-a00c-490820f66d28)

### *로그아웃

![3](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/a61bcc61-bd7a-4288-b181-81499bad6404)
![3-1](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/18c67909-85fa-4eb0-a856-89b2f24e540d)

### *회원가입

![4](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/c24eef12-fdcf-4001-8d70-d66352f73c65)
(필수값 미입력)
![4-1](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/4c8537e6-fe68-4628-a2be-36ea7cda3a67)
(중복값 입력)
![4-2](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/f73bb0fd-1d47-4e90-9e25-93582377c047)

### *프로필 페이지
![5](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/1ab75aec-f47a-4d8a-b4e9-018327ece9d6)

토큰없이(로그인 없이) 프로필을 조회한 경우
![5-1](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/2b98269f-093e-4d4e-a0bb-a181ff9332d4)

### *Article 생성
![상품생성 정상기능](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/01b7274d-0c63-4f51-b4ac-ed5b237f9a56)

게시글 생성시 로그인 필요

![상품생성 시 로그인 필요](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/49a51725-fdd3-416f-8dc0-698c44f2491f)
### *Article 삭제 

![상품삭제 정상기능](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/c943a0be-286c-47fa-814e-fef09cd87c93)

삭제시 작성자 검증
![상품삭제 시 작성자 검증](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/3269d3c8-2ba1-462e-88a0-17363547e7af)
![상품삭제 기능 후 글 사라짐](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/53adf854-cf9d-4b43-a1ce-9927afac25bb)

### *Article 수정

![상품수정 정상기능](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/e870da65-c124-4ec3-b13a-d7e4e995f834)

수정시 작성자검증

![상품수정 시 작성자 검증](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/a6c7d8e7-95c8-4d2b-a67c-7b1f52e241a6)


### *Article 정렬

게시글 목록

![게시글 목록조회(기본정렬 좋아요 많은순, 최신순)](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/9a2c6f53-7ada-44ac-b9b8-931f0b261ebd)

최신순
![상품정렬, 최신순](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/8f3efec4-8be9-498d-a839-5c1f5ec47e5c)

좋아요순
![상품정렬, 좋아요 많은 순](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/d7b75cc7-106b-4385-b913-f87cb4d3992b)

### *Article 검색
내용으로 검색
![상품검색, 내용으로 찾기](https://github.com/hyunki0523/SpartaNewsPjt/assets/159873023/2058d076-1a06-4788-a226-67c4c7f8c495)

