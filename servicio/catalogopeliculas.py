from dominio.pelicula import Pelicula
import os

class Catalogopeliculas:
    ruta_archivo= '/home/david/Documentos/programacion/catalogo_peliculas/peliculas.txt'
    
    def __init__(self,catalogo):
        self.catalogo
    
    @staticmethod    
    def agregar_pelicula (pelicula):
        pelicula= str(pelicula)
        agregar_pelicula = open(Catalogopeliculas.ruta_archivo, 'a')
        agregar_pelicula.write (pelicula.__str__()+ '\n')
        agregar_pelicula.close()
        
    @staticmethod
    def listar_peliculas ():
        listado = open(Catalogopeliculas.ruta_archivo, 'r')
        print (listado.read())
        listado.close
         
    @staticmethod    
    def eliminar():
        os.remove(Catalogopeliculas.ruta_archivo)    
            
