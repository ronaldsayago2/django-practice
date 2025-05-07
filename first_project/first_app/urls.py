from django.contrib import admin
from django.urls import path
from first_app import views

urlpatterns = [

    path('',views.index2),
    path('first_app',views.index3, name = 'access_history'),
    path('users', views.users, name = 'users_list'),
    path('form_page', views.form_name_view, name = 'form_route'),
    path('form_signup', views.form_signup_view, name = 'form_signup'),
    path('user_login', views.login_user, name = 'user_login'),
    path('user_logout', views.logout_user, name = 'user_logout'),




    
]