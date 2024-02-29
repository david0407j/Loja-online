from django.urls import reverse
from loja.django_assertions import assert_contains
import pytest


@pytest.fixture
def resp(client, db):
    return client.get(reverse('vendas:produtos', args=('outros',)))


def test_titulo_outros(resp):
   assert_contains(resp, 'produtos' )


def test_status_code(resp):
    assert resp.status_code == 200


def test_variedade(resp):
   assert_contains(resp, 'variedade' )



def test_titulo_importados(resp):
   assert_contains(resp, 'importados' )


