import sys
sys.path.append('src')
from calcul_tarif import calcul_tarif
import pytest



@pytest.fixture
def fix_setUpTearDown():
    print("before")
    yield
    print("after")

def test_enfant_parisien1(fix_setUpTearDown):
#    mocker.patch('calcul_tarif.calcul_tarif.get',return_value=1.4)
    print("toto")
    calcul = calcul_tarif()
    y=calcul.tarif(4,True)
    assert y == 1.5
def test_adulte_touriste(mocker):
    mocker.patch('calcul_tarif.calcul_tarif.get',return_value=1.4)
    calcul = calcul_tarif()
    y=calcul.tarif(20,True)
    assert y == 2.8
def test_adulte_parisien(mocker):
    mocker.patch('calcul_tarif.calcul_tarif.get',return_value=1.4)
    calcul = calcul_tarif()
    y=calcul.tarif(20,False)
    assert y == 1.4
def test_enfant_parisien(mocker):
    mocker.patch('calcul_tarif.calcul_tarif.get',return_value=1.4)
    calcul = calcul_tarif()
    y=calcul.tarif(7,False)
    assert y == 0.7