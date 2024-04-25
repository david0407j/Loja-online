from django.urls import path
from loja.modelos import views



app_name = 'modelos'
urlpatterns = [
    path('', views.index),
    path('update/<int:pessoa_id>/', views.update, name='update_pessoa')
]