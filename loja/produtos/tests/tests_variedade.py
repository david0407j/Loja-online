from django.urls import reverse
from loja.django_assertions import assert_contains
import pytest


@pytest.fixture
def resp(client, db):
    return client.get(reverse('produtos:variedade', args=('variedade',)))


def test_titulo_produtos(resp):
   assert_contains(resp, 'produtos' )



def test_varidade_produtos(resp):
    assert resp.status_code == 200


def test_variedades(resp):
   assert_contains(resp, 'Variedade' )



def test_titulo(resp):
   assert_contains(resp, 'Produtos importados' )


