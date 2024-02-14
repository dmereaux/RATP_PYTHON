import sys
sys.path.append('src')
from calcul_tarif import calcul_tarif
import pytest
from unittest.mock import Mock


@pytest.fixture
def fix_setUpTearDown():
    print("before")
    yield
    print("after")

def test_one(mocker):
    mocker.patch('calcul_tarif.calcul_tarif.get',return_value=1.4)
    print("test")
    calcul = calcul_tarif()
    y=calcul.tarif(4,True)
    assert y == 1.5
