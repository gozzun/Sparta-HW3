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
  
<피드백 사항>
- readme 내용에서 과제에 대한 설명이 있어서 좋아요. 추가적으로 ERD에 대한 내용과 구현기간에 대해서도 같이 작성해주시면 매우 좋습니다.
  그래야 DB 구조를 한눈에 직관적으로 파악할 수가 있습니다.
- 기본요건을 모두 구현하셨네요! 정말 정말 매우 훌륭하게 고생하셨습니다. 
- from 으로 필요한 라이브러리를 포함하는 코드는 정리할 필요가 있습니다.
  from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

이런식으로 되어있는데

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status

from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .serializers import UserSerializer

from .models import User
이런식으로 이쁘게 나눠주세요. 가독성이 좋아야 해당 소스코드에 어떤 라이브러리들을 사용하는지 파악하기 쉬워요.
- serializers 부분이 다소 빈약해 보이네요. 조금 더 필요한 기능들을 시도하고 추가해보시면 좋을것같아요.
- 아직 초기단계니까 코드에 주석을 다는 습관을 들이시는것을 강력하게 추천드립니다.
- commit 내용이 너무 부실하고 적어요. 작은 코드단위로 최대한 상세한 commit내용으로 작성을 해주시면 회사에서 매우 좋아합니다.
  그리고 전문성있어보이는 효과가 있어요.
- 매우 고생하셨고 우리 얼마 안남은 프로젝트들도 파이팅입니다! ;)
