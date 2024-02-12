import sys
sys.path.append('src')
from calcul_tarif import calcul_tarif


def test_one():
    calcul = calcul_tarif()
    y=calcul.tarif(4,True)
    assert y == 1.5
