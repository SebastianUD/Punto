from punto import Punto

class Programa:
    def __init__(self):
        messi=Punto()
        elbicho=Punto()

        messi.x=8
        messi.y=2

        elbicho.x=9
        elbicho.y=9

        self.a=elbicho.calcular_distancia(messi)

runnig=Programa()

print(runnig.a)