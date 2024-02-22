from django.urls import reverse
from loja.django_assertions import assert_contains
import pytest


@pytest.fixture
def resp(client):
    return client.get(reverse('produto:outros', args=('outros',)))



def test_status_code(resp):
    assert resp.status_code == 200

def test_titulo(resp):
   assert_contains(resp, 'outros' )



def test_produtos_(resp):
   assert_contains(resp, 'variedades produtos' )



def test_titulo_importados(resp):
   assert_contains(resp, 'Produtos importados' )


