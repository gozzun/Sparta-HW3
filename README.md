<과제 설명>  
Django DRF를 이용하여 HW2(스파르타마켓) 재구현  

<기본 조건>  
-각 유저는 자신의 물건 등록  
-지역별 유저 고려X  
-accounts/products 앱 필수  
-.gitignore  
-DRF 집중, Postman 사용 권장  
  
<필수 구현>  
1. Accounts  
-회원가입: /api/accounts, POST  
-로그인: /api/accounts/login, POST  
-프로필 조회: api/accounts/<str:username>, GET  

*accounts 구현: UserSerializer 사용, 함수형 뷰  
**비밀번호 해싱 구현: make_password(password)  

2. Products  
-상품 등록: /api/products, POST  
-상품 목록 조회: /api/products, GET  
-상품 수정: /api/products/<int:productId>, PUT  
-상품 삭제: /api/products/<int:productId>, DELETE  

*products 구현: ProductSerializer 사용, 클래스형 뷰  
**페이지네이션: generics.ListCreateAPIView -> PageNumberPagination  

<추가로 구현해야할 사항 (선택 기능 + α)>  
-로그아웃, 본인 정보 수정, 패스워드 변경, 회원 탈퇴, 팔로잉, 페이지네이션 및 필터링, 카테고리, 좋아요, 태그  
  
※비록 DRF에 대한 이해가 부족하여 복습을 하느라 시간 부족으로 인해 선택 기능 구현까지는 하지 못했지만, 시간이 넉넉하게 주어졌다면 선택 기능까지는 금방 구현 가능할 것 같습니다.
