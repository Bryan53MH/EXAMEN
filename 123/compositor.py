from oyente import Oyente

class Compositor(Oyente):
    lugar_nacimiento  = str 
    edad              = int    
    
    
    def __init__(self, id, nombre, lugar_nacimiento, edad):
        super().__init__(id, nombre)
        self.lugar_nacimiento = lugar_nacimiento
        self.edad             = int