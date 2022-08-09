from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from contar_caloria.models import Calorias, TipoRefeicao
import pytest 

# Create your tests here.
@pytest.fixture
def _alimento():
    return {'descricao': 'franguinho', 'calorias': 100, 'quantidade': 3}


def test_status_ok(client, db):
    resposta = client.get(reverse('home'))
    assert resposta.status_code == 200

def test_template_home(client, db):
    resposta = client.get(reverse('home'))
    assertTemplateUsed(resposta, 'contar_caloria/pg_inicial.html')

def test_multiplica_calorias_pela_quantidade(_alimento):
    qt_alimento = _alimento['quantidade']
    caloria = _alimento['calorias']
    multiplicacao = caloria * qt_alimento
    assert multiplicacao == 300
