from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # Built-in login/logout views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Dashboard view
    path('dashboard/', views.dashboard, name='dashboard'),
]
