
import pytest
from django.urls import reverse
from loja.django_assertions import assert_contains

@pytest.fixture
def resp(client):
   resp = client.get(reverse('base:home'))
   return resp

def test_status_code(resp):
    assert resp.status_code == 200

def test_title(resp):
   assert_contains(resp, '<title>Reizinho-imports- home</title>' )

def test_home_link(resp):
   assert_contains(resp, f'href="{reverse("base:home")}">Reizinho-importe</a>' )

def test_conteudo_link(resp):
    assert_contains(resp, 'href="http://127.0.0.1:8000/aperitivos/masculino"')


def test_email(resp):
   assert_contains(resp, 'reizinhomp@gmail.com')


def test_conteudo_link_infatil(resp):
    assert_contains(resp, 'href="http://127.0.0.1:8000/modelos/femenina"')


def test_conteudo_link(resp):
    assert_contains(resp, 'href="http://127.0.0.1:8000/produtos/outros"')






