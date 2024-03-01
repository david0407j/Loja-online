from django.urls import reverse
from loja.django_assertions import assert_contains
import pytest


@pytest.fixture
def resp(client, bd):
    return client.get(reverse('produtos:outros', args=('outros',)))


def test_titulo_produtos(resp):
   assert_contains(resp, 'variedade produtos' )



def test_varidade_produtos(resp):
    assert resp.status_code == 200


def test_Produtos_(resp):
   assert_contains(resp, 'Variedades de Produtos' )



def test_titulo(resp):
   assert_contains(resp, 'Produtos importados' )


