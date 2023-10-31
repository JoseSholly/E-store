from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



app_name= 'users'
urlpatterns= [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile')
]

# template_name='users/logout.html'