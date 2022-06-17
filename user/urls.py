from django.urls import path, include
from user import views

urlpatterns = [
    path('', views.UserApiView.as_view()),
    path('signup/', views.UserView.as_view()),
    path('login/', views.UserApiView.as_view()),
    path('logout/', views.UserApiView.as_view()),
]
