from oyente import Oyente


class Cancion(Oyente):
    id              = int
    nombre_cancion  = str
    grupo           = str  
    
    def __init__(self, id_oyente, nickname, id, nombre_cancion, grupo):
        super().__init__(id_oyente,nickname)
        self.id             = id   
        self.nombre_cancion = nombre_cancion
        self.grupo          = grupo
 
 
 #******** HERENCIA DENTRO DEL ARCHIVO***********
 
        
class InfoAdd(Cancion):
    likes             = int   
    fecha_lanzamiento = str
    
    def __init__(self, id_oyente, nickname, id, nombre_cancion, grupo, likes, fecha_lanzamiento):
       super().__init__(id_oyente, nickname, id, nombre_cancion, grupo)
       self.likes             = likes
       self.fecha_lanzamiento = fecha_lanzamiento
       
       
    def __str__(self):
        return f'La cancion {self.nombre_cancion} tocada por el grupo {self.grupo} recibiendo la cantidad de {self.likes} likes pese a los años de haber sido estrenada, esta fue estrenada el {self.fecha_lanzamiento} tiene un id {self.id} dentro de la plataforma, fue vista por {self.nickname} con id del oyente'
    