import django.http 
import pytest
from django.urls import reverse
from loja.django_assertions import assert_contains

@pytest.fixture
def resp(client):
   resp = client.get(reverse('loja:home'))
   return resp

def test_status_code(resp):
    assert resp.status_code == 200

def test_titulo(resp):
   assert_contains(resp, '<title>Reizinho-imports</title>' )

def test_home_link(resp):
   assert_contains(resp, f'href="{reverse("loja:home")}">Reizinho-imports</a>' )


def test_email(resp):
   assert_contains(resp, 'Reizinho-imports@hotmial.com')


def test_img(resp):
   assert_contains(res, 'img/mila.ico')


def test_title(resp):
   assert_contains(resp, '<title>Produtos da loja </title>' )


