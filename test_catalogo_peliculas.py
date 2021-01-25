from servicio.catalogopeliculas import Catalogopeliculas
from dominio.pelicula import Pelicula

class Menu1:
    
    print('---------------------------------------------')
    print('Menu de Opciones')
    print('---------------------------------------------')
    print('\n1. Agregar pelicula')
    print('2. Lista de peliculas')
    print('3. Eliminar catalogo de peliculas')
    print('4. Salir\n')
    
    seleccion=0
    
    while True:
        try:        
            seleccion= int (input('Selecciona una opcion: ')) 
        
        except Exception as e:
            print(type (e))
            print('Asegurate de introducir opciones validas')  
        finally:
            pass 
        
        if seleccion == 1:
            class Menu2:
                
                print('---------------------------------------------')
                print('Agregar pelicula')
                print('---------------------------------------------\n')
                print('Escribe la pelicula a agregar: ')
                inputpelicula= (input ())
                pelicula= Pelicula (inputpelicula)
                #Pelicula.set_nombre(inputpelicula)
                Catalogopeliculas.agregar_pelicula(pelicula)
            
            continue
        if seleccion == 2:
            class Menu3:
                print('---------------------------------------------')
                print('Lista de peliculas')
                print('---------------------------------------------\n')
                Catalogopeliculas.listar_peliculas()
                
                    
        if seleccion == 3:
            class Menu4:
                Catalogopeliculas.eliminar()
            #continue
            
        if seleccion == 4:
            exit ()   
exit()        

    
    
