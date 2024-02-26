from calcul_tarif import calcul_tarif
from robot.api.deco  import  keyword, library
calcul = calcul_tarif()
@keyword('calcul tarif ticket metro')
def k_tarif(age,touriste):
    y=calcul.tarif(int(age),touriste)
    return y
