from oyente     import  Oyente
from canciones  import  Cancion
from canciones  import  InfoAdd
from compositor import  Compositor
from categoria  import  Categoria


class Informacion:
    pais_origen  = str
    visitas      = int
    canciones    = InfoAdd("","","","","","","")
    compositor   = Compositor("","","","")
    oyente       = Oyente("","")
    categoria    = Categoria("","")
    
    def __init__(self, pais_origen, visitas, canciones, compositor, oyente, categoria):
        self.pais_origen = pais_origen
        self.visitas     = visitas
        self.canciones   = canciones 
        self.compositor  = compositor
        self.oyente      = oyente 
        self.categoria   = categoria