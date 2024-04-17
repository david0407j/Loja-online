
from django.urls import path

from loja.base.views import home
from django.contrib.auth import views as auth_views

app_name = 'base'


urlpatterns = [
    path('', home, name='home'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
