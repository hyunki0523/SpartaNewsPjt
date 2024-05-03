
## * Description

   * ### Project name : Sparta Market 
스파르타만의 중고거래 플렛폼을 구현

   * ### Project duration : 2024-04-12 ~ 2024-04-09
개인프로젝트이므로 본인이 설계 구현 모두 담당

## * Environment & Tech stack
Window 환경에서 Pycham 사용. 

Python(3.10) , Django Framework (4.2.11) , Bootstrap 사용

Database : SQLite3 


## * Prerequisite

Package|Version
---|---|
asgiref            |3.8.1
backports.zoneinfo |0.2.1
Django             |4.2.11
django-environ     |0.11.2
pip                |24.0
setuptools         |68.2.0
sqlparse           |0.5.0
typing_extensions  |4.11.0
tzdata             |2024.1
wheel              |0.41.2


## * Roadmap

- [x] 회원기능 (Accounts, app name: account)
    - [x] 회원가입, 로그인, 로그아웃
    - [x] 관리자계정
- [x] 프로필 페이지
  - [x] 찜 기능 (check_users:products/model/Post)
  - [x] 팔로우 기능 (followings:accounts/model/User)
  - [ ] 개인프로필 설정(이미지, 태그)
- [x] 게시글 CRUD (Products, app name: post)
    - [x] 게시글 기능(제목, 내용, 가격)
    - [x] 로그인 권한을 바탕으로 CRUD 구현
    - [x] 댓글 CRUD


-  TODO
- [ ] 이미지(media, Pillow)
    - [ ] 개인프로필
    - [ ] 게시글 이미지첨부
- [ ] 게시글 검색 및 정렬

## * Use

홈페이지의 접속과 동시에 모든 게시글 확인할 수 있는 메인페이지로 이동합니다.<br/> 
이후 링크를 통해 로그인, 회원가입 페이지로, 게시글의 상세페이지로 이동이 가능합니다.<br/>
로그인을 통해 권한을 부여 받은경우 글작성페이지 , 프로필 페이지로 이동이 가능하고<br/>
회원정보수정, 회원탈퇴 기능이 이용가능 합니다. <br/>
추가적으로 게시글의 찜 버튼과 상세페이지 내부의 댓글기능이 활성화 되며 <br/>
타 이용자의 프로필 페이지(작성자의 프로필 버튼으로 이동가능) 방문시 팔로우기능이 활성화 됩니다. <br/>
나의 프로필에서 본은계정을 팔로우한 수 를 확인할 수 있으며, 게시글 목록과 찜 목록을 확인하고 바로 이동가능합니다. <br/>
게시글의 상세페이지에서 본인이 작성한 게시글 ,댓글 인경우 글 수정 및 삭제가 가능합니다. <br/><br/>

## * ERD<br/>
![SpartaNews ERD](https://github.com/hyunki0523/SpartaNewsPjt/assets/122522460/8c69f313-7ba6-463b-bd98-c0343999e0f4)
<br/><br/>


