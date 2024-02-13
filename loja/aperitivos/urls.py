from django.urls import path
from loja.aperitivos.views import masculino



app_name = 'aperitivos'
urlpatterns = [
    path('<slug:nome>', masculino, name='masculino'),
]