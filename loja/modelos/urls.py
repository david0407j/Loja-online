from django.urls import path
from loja.modelos.views import femenina



app_name = 'modelos'
urlpatterns = [
    path('<slug:slug>', femenina, name='femenina'),
]