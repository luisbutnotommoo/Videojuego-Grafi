from PersonajeLin.blue_multiverso.machote.dibuja2 import clasePersonajeBlue as CP

class pesonajeLinEmocionesJuego:

    def __init__(self, emocion):
        self.emocion=emocion
        self.instancia=CP()
        

    def personaje(self, emocion):
        if emocion==0:
            self.instancia.draw()
        if emocion==2:
            self.instancia.draw_happy()
        if emocion==1:
            self.instancia.draw_angry()

        