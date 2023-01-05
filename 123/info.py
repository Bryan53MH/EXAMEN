from oyente      import  Oyente
from canciones   import  Cancion
from canciones   import  InfoAdd
from compositor  import  Compositor
from categoria   import  Categoria
from informacion import Informacion


class Info(Informacion):
    pais_productor =  str
    cds_vendidos   =  int
    
    
    def __init__(self, pais_origen, visitas, canciones, compositor, oyente, categoria, pais_productor, cds_vendidos):
        super().__init__(pais_origen, visitas, canciones, compositor, oyente, categoria)
        self.pais_productor  = pais_productor
        self.cds_vendidos    = cds_vendidos