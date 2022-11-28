from django.urls import path, include

from . import views

urlpatterns = [
    path('usersAPI/', views.CustomUserAPIView.as_view()),
    path('usersAPI/<str:pk>/', views.CustomUserAPIView.as_view()),
]