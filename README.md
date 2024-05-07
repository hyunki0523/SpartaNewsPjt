
## * Description

   * ### Project name : Sparta News 
스파르타만의 뉴스 제공 서비스 구현

레퍼런스 : https://news.hada.io/

   * ### Project duration : 2024-05-03 ~ 2024-05-10


* ### Tech Explorers :
|----|----|----|----|
* 황승환	👑  |	INFP |	https://github.com/hideoutoasis/spartamarket_DRF_by_HSH |	https://blog.naver.com/sunbook24
* 김도연	member |	ISTJ |		| https://sparkly-field-a92.notion.site/KDY-S-BLOG-d2eabf21b14b497eb4842a696977d06c?pvs=74	
* 이현기	member |	ISTP |	https://github.com/hyunki0523 |	https://blog.naver.com/dldl5040
* 옹석현	member |	ISTP |	https://github.com/ongsh98 |	https://blog.naver.com/dhd9808	

## * Environment & Tech stack
Window 환경에서 Pycham 사용. 

VisualStudio ,Python(3.10) , Django Framework (4.2.11) , Bootstrap 사용

Database : SQLite3 

API 기능 점검 : Postman 이용.

## * Prerequisite

Package|Version
-----------------

|----|----|----|----|

alembic                        | 1.13.1
asgiref                        | 3.7.2
asttokens                      | 2.4.1
beautifulsoup4                 | 4.12.3
blinker                        | 1.7.0
bs4                            | 0.0.2
certifi                        | 2023.11.17
cffi                           | 1.16.0
charset-normalizer             | 3.3.2
click                          | 8.1.7
colorama                       | 0.4.6
cryptography                   | 42.0.1
decorator                      | 5.1.1
Django                         | 4.2
django-environ                 | 0.11.2
django-extensions              | 3.2.3
django-seed                    | 0.3.1
djangorestframework            | 3.15.1
djangorestframework-simplejwt  | 5.3.1
et-xmlfile                     | 1.1.0
exceptiongroup                 | 1.2.0
executing                      | 2.0.1
Faker                          | 24.4.0
Flask                          | 3.0.2
Flask-Migrate                  | 4.0.5
Flask-SQLAlchemy               | 3.1.1
greenlet                       | 3.0.3
idna                           | 3.6
ipython                        | 8.22.2
itsdangerous                   | 2.1.2
jedi                           | 0.19.1
Jinja2                         | 3.1.3
Mako                           | 1.3.2
MarkupSafe                     | 2.1.5
matplotlib-inline              | 0.1.6
openpyxl                       | 3.1.2
parso                          | 0.8.3
pexpect                        | 4.9.0
pillow                         | 10.2.0
pip                            | 24.0
prompt-toolkit                 | 3.0.43
psycopg2                       | 2.9.9
ptyprocess                     | 0.7.0
pure-eval                      | 0.2.2
pycparser                      | 2.21
Pygments                       | 2.17.2
PyJWT                          | 2.8.0
pypng                          | 0.20220715.0
python-dateutil                | 2.9.0.post0
pytz                           | 2023.3.post1
qrcode                         | 7.4.2
requests                       | 2.31.0
Send2Trash                     | 1.8.2
setuptools                     | 65.5.0
six                            | 1.16.0
slack-bolt                     | 1.18.1
slack_sdk                      | 3.26.2
soupsieve                      | 2.5
SQLAlchemy                     | 2.0.27
sqlparse                       | 0.4.4
stack-data                     | 0.6.3
toposort                       | 1.10
traitlets                      | 5.14.2
typing_extensions              | 4.10.0
tzdata                         | 2024.1
urllib3                        | 2.1.0
wcwidth                        | 0.2.13
Werkzeug                       | 3.0.1


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
## * Use

별도의 템플릿 구현하지 않았으므로, postman 과 같은 API platform 을 통해 확인가능합니다.
구현한 기능은 크게 유저, 게시글 로 나눌수 있으며
유저의 경우
 회원가입, 로그인(JWT 사용, Token refresh 구현),
 로그아웃, 개인 프로필 페이지( '좋아요' 한 목록과 내가 작성한 글 확인가능)
게시글의 경우
 기본적으로 게시글을 목록형태로 확인가능하고 , 검색과 정렬 기능(좋아요 순, 최신 순)을 지원합니다.
 로그인을 한 경우 생성이 가능하고, 수정 및 삭제의 경우 작성자와 동일한 경우만 가능합니다.
 댓글의 CRUD 기능을 지원합니다.


  
## * ERD<br/>
![SpartaNews ERD](https://github.com/hyunki0523/SpartaNewsPjt/assets/122522460/8c69f313-7ba6-463b-bd98-c0343999e0f4)
<br/><br/>


