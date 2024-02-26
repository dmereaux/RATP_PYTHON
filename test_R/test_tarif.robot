*** Settings ***
Library     ../src/calcul_tarif.py
Library     ../src/wrapper.py
*** Test Cases ***
test frais
   ${x}   calcul_tarif.Tarif  ${7}   True
   Should Be Equal As Numbers  ${x}   1.5
test frais 2
   ${x}  calcul tarif ticket metro  20  False
   Should Be Equal As Numbers   ${x}  3.0