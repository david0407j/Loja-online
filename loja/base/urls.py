from django.urls import path
from loja.base.views import home
from loja.base import views

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('register/', views.register, name='register'),
]

