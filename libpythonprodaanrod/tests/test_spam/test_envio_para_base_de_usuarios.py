from unittest.mock import Mock

import pytest

from libpythonprodaanrod.spam.main import EnviadorDeSpam
from libpythonprodaanrod.spam.modelos import Usuario



@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Danilo', email='daanrod93@gmail.com'),
            Usuario(nome='Joyce', email='daanrod93@gmail.com')
        ],
        [
            Usuario(nome='Danilo', email='daanrod93@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'daanrod93@gmail.com',
        'Vambora!',
        'Conseguimos primo'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Danilo', email='daanrod93@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'sharp.aedes@gmail.com',
        'Vambora!',
        'Conseguimos primo'
    )
    enviador.enviar.assert_called_once_with(
        'sharp.aedes@gmail.com',
        'daanrod93@gmail.com',
        'Vambora!',
        'Conseguimos primo'
    )

