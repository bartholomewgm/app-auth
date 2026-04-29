from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, dashboard

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]
