from django.urls import path, include
from . import views


app_name= 'payment'

urlpatterns = [
    path('process/', views.payment_process, name= 'process'),
    path('completed/', views.payment_completed, name= 'completed'),
    path('canceled', views.payment_canceled, name='canceled')
]