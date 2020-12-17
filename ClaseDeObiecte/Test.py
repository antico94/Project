from viata import Intrebari
lista_intrebari=[("Culoarea bananei?"),("Culoarea portocalei?"),("Culoarea rosiei?")]
lista_raspunsuri=[("Galben"),("Portocaliu"),("Rosu")]
Intrebari(lista_intrebari[0],lista_raspunsuri[0])
Intrebari(lista_intrebari[1],lista_raspunsuri[1])
Intrebari(lista_intrebari[2],lista_raspunsuri[2])

def test(plm):
    a=0
    for intrebari in lista_intrebari:
        raspuns=input(lista_intrebari[a])
        a+=1
        if raspuns==Intrebari(lista_intrebari)

