import pytest
from django.urls import reverse
from loja.django_assertions import assert_contains

# tests navb link dos produtos


@pytest.fixture
def resp(
    client,
):
    resp = client.get(reverse("base:home"))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, "<title>Reizinho-imports- home</title>")


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Reizinho-importe</a>')


def test_pagina_deve_conter_o_link_produtos_masculinos(resp):
    assert_contains(
        resp, reverse("produtos:produto", kwargs={"nome_categoria": "Masculino"})
    )


def test_email(resp):
    assert_contains(resp, "reizinhomp@gmail.com")


def test_pagina_o_link_infantil(resp):
    assert_contains(
        resp, reverse("produtos:produto", kwargs={"nome_categoria": "Infantil"})
    )


def test_pagina_deve_conter_o_link_produtos(resp):
    assert_contains(
        resp, reverse("produtos:produto", kwargs={"nome_categoria": "Produtos"})
    )


def test_pagina_deve_conter_o_link_feminina(resp):
    assert_contains(
        resp, reverse("produtos:produto", kwargs={"nome_categoria": "Feminina"})
    )


def test_pagina_deve_conter_o_link_cosmetico(resp):
    assert_contains(
        resp, reverse("produtos:produto", kwargs={"nome_categoria": "Cosmético"})
    )
