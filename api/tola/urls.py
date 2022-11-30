from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path('usersAPI/', views.CustomUserAPIView.as_view()),
    path('usersAPI/<str:pk>/', views.CustomUserAPIView.as_view()),
    path('maxAPI/', views.MaxAPIView.as_view()),
    path('maxAPI/<str:pk>/', views.MaxAPIView.as_view()),
    path('exerciseAPI/', views.ExerciseAPIView.as_view()),
    path('exerciseAPI/<str:pk>/', views.ExerciseAPIView.as_view()),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]