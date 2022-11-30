from django.urls import path, include

from . import views

urlpatterns = [
    path('usersAPI/', views.CustomUserAPIView.as_view()),
    path('usersAPI/<str:pk>/', views.CustomUserAPIView.as_view()),
    path('maxAPI/', views.MaxAPIView.as_view()),
    path('maxAPI/<str:pk>/', views.MaxAPIView.as_view()),
    path('exerciseAPI/', views.ExerciseAPIView.as_view()),
    path('exerciseAPI/<str:pk>/', views.ExerciseAPIView.as_view()),
]