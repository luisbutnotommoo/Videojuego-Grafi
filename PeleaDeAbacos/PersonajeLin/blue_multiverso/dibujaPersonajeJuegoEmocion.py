from PersonajeLin.blue_multiverso.machote.dibuja import clasePersonajeBlue as CP

class pesonajeLinEmocionesJuego:

    def __init__(self, emocion):
        self.emocion=emocion
        self.instancia=CP()
        

    def personaje(self):
        if self.emocion==0:
            self.instancia.draw()
        