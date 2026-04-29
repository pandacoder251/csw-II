from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
urlpatterns = [
 #path('login/', views.user_login, name='login'),
 path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
 path('logout/', auth_views.LogoutView.as_view(), name='logout'),
 path('',views.dashboard, name='dashboard'),
 path('password_change', auth_views.PasswordChangeView.as_view(template_name='account/password_change_form.html'), name='password_change'),
 path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),
]
