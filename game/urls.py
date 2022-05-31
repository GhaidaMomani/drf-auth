from lib2to3.pgen2 import token
from django.urls import path
from .views import GameListView, GameDetailView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', GameListView.as_view(), name="game_list"),
    path('game-detail/<int:pk>', GameDetailView.as_view(), name="game_detail"),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
  

]


