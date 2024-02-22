from django.urls import reverse
from loja.django_assertions import assert_contains
import pytest


@pytest.fixture
def resp(client,):
    return client.get(reverse('aperitivos:masculino', args=('masculino',)))



def test_titulo_masculino(self,):
   assert_contains(self, 'produto masculino')


def test_status_code(self,):
    assert self.status_code == 200



def test_produtos(self):
   assert_contains(self, src="produto.img.url ")