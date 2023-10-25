from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



app_name= 'users'
urlpatterns= [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]

# template_name='users/logout.html'