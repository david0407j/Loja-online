from django.urls import reverse
from loja.django_assertions import assert_contains
import pytest


@pytest.fixture
def resp(client, db):
    return client.get(reverse('aperitivos:masculino', args=('masculino',)))



def test_titulo_masculino(resp,):
   assert_contains(resp, 'masculino')


def test_status_code(resp,):
    assert resp.status_code == 200



def test_produtos_masculino(resp):
   assert_contains(resp, 'produtos')