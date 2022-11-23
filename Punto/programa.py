from punto import Punto

class Programa:
    def __init__(self):
        self.messi=Punto()
        self.elbicho=Punto()

        self.messi.x=8
        self.messi.y=2

        self.elbicho.x=9
        self.elbicho.y=9

        self.a=self.elbicho.calcular_distancia(self.messi)

runnig=Programa()

print(runnig.a)