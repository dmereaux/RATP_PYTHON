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

    calcul_tarif.get.assert_called_once_with()
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
@pytest.mark.parametrize('age,tourist,tarif_attendu', [
    # each element of this list will provide values for the
    # topics "value_A" and "value_B" of the test and will
    # generate a stand-alone test case.
    (20, True,3.0),
    (7,True,1.5),
    (7,False,0.75),
])    
def test_tarif(age,tourist,tarif_attendu):
    calcul = calcul_tarif()
    y=calcul.tarif(age,tourist)
    assert y == tarif_attendu