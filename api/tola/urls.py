from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

# router.register(r'user_program_view_set', views.user_programViewSet)

urlpatterns = [
    path('user/signup/', views.CustomUserAPIView.as_view(), name="create_user"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('usersAPI/', views.CustomUserAPIView.as_view()),
    path('usersAPI/<str:pk>/', views.CustomUserAPIView.as_view()),
    path('maxAPI/', views.MaxAPIView.as_view()),
    path('maxAPI/<str:pk>/', views.MaxAPIView.as_view()),
    path('exerciseAPI/', views.ExerciseAPIView.as_view()),
    path('exerciseAPI/<str:pk>/', views.ExerciseAPIView.as_view()),
    path('usergymAPI/', views.UserGymAPIView.as_view()),
    path('usergymAPI/<str:pk>/', views.UserGymAPIView.as_view()),
    path('gymAPI/', views.GymAPIView.as_view()),
    path('gymAPI/<str:pk>/', views.GymAPIView.as_view()),
    path('addUserToProgram/<int:program_id>/', views.addUserToProgram),
]