import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Video Aperitivo: Motivação',
        'Tempo para ser programador'
    ]
)
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)


# def test_conteudo_video(resp):
#     assert_contains(resp, 'src="https://player.vimeo.com/video/799826779?h=be5ee2d29c"')
