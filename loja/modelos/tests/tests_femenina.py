from django.urls import reverse
from loja.django_assertions import assert_contains
import pytest


@pytest.fixture

def resp(client, db):
    return client.get(reverse('modelos:femenina', args=('femenina',)))


def test_titulo_femenina(resp):
   assert_contains(resp, 'femenina' )



def test_status_code(resp):
    assert resp.status_code == 200


def test_produtos_importados(resp):
   assert_contains(resp, 'importados' )
