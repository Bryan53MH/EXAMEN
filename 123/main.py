from oyente      import  Oyente
from canciones   import  Cancion
from canciones   import  InfoAdd
from compositor  import  Compositor
from categoria   import  Categoria
from informacion import  Informacion
from info        import  Info


if __name__ == "__main__":
    
    cancion1  = InfoAdd(1314, "brYan53MH", 123980, "ONE", "METALLICA", 274000000, "04/10/1988") 
    cancion2  = InfoAdd(2567, "Juanito777", 24567, "LA MAGIA", "LITTLE JESUS", 30977223, "12/06/2016")
    cancion3  = Cancion(9256, "pepelucho12", 3561234, "DEAD MEMORIES", "SLIPKNOT")
    
    
    categoria1  =Categoria(234, "TRASH METAL")
    categoria2  =Categoria(452, "NEW METAL")
    
    compositor1  = Compositor(324, "JAMES HELTFIELD", "CALIFORNIA", 56)
    compositor2  = Compositor(2325, "COREY TAYLOR", "DES MOINES", 48)
     
    oyente1  = Oyente(23824, "brYan53MH")
    oyente2  = Oyente(78934, "pepelucho12")
    
    informacion1  = Informacion("ESTADOS UNIDOS", 274.23445, compositor1, oyente2, categoria1, cancion1)
    informacion2  = Informacion("ESTADOS UNIDOS", 459.23562, compositor2, oyente2, categoria1, cancion2)
    
    informacion3 = Info("USA", 3.5687895, "ESTADOS UNIDOS", 274.23445, compositor1, oyente2, categoria1, cancion1)
    informacion4 = Info("INGLATERRA", 6.567734, "ESTADOS UNIDOS", 459.23562, compositor2, oyente2, categoria1, cancion2)
    
    
    oyente3 = Oyente(1234, "Goku782")
    oyente4 = Oyente(674534, "lucho42")
    
    
    #****LA CLASE CON METODO*****
    
    print("*********Pregunta 1 *********")
    
    
    print(oyente3)
    print(oyente4)
    print(vars(oyente4))
    
    
    print("*********Pregunta 2************")
    
    print(vars(categoria1))
    
    
    print("*********Pregunta 3************")
    
    print(cancion1)
    print(cancion2)
    
    
    print("*********Pregunta 4************")
    
    print("COMPOSITOR")
    print(vars(compositor1))
    
    print("*********Pregunta 5************")
    
    print(vars(informacion3))
    
    
    
    
    
    
    
    
    
    
    print("**************** CLASE CON METODO ***********")
    print(" TODA LA INFORMACION")
    print(vars(cancion1))
    print(" ")
    
    print("CANCIONES")
    print(vars(cancion3))
    print(" ")
    
    print("CATEGORIA")
    print(vars(categoria1))
    print(" ")
    
    print("COMPOSITOR")
    print(vars(compositor1))
    
    #********* METODO STR *********
    
    print("************** METODO STR ****************")
    print(cancion1)
    print(" ")
    print(cancion2)
    
    
    #**************OBJETOS DENTRO DE OBJETOS*************
    
    print("*********** OBJETOS DENTRO DE OBJETOS************")
    print(vars(informacion1))  
    print(" ")  
    print(vars(informacion2))
