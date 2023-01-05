class Oyente:
    id_oyente  = int
    nickname   = str  
    
    
    def __init__(self, id_oyente, nickname):
        self.id_oyente = id_oyente
        self.nickname  = nickname
        
        
        
        
    def __str__(self):
        return f' El ID de nuestro oyente es: {self.id_oyente} y su nick name es: {self.nickname}'
    
    
    
    
    
        
        
        
        