"""
from src.models.Usuario import Usuario
from src.models.Tarea import Tarea
"""
from src.services.Task_Service import Task_Service
import logging 

logging.basicConfig(
     level=logging.INFO, 
     format="%(asctime)s %(levelname)s %(message)s"
)


def main(): 

      print("\n ---------------- Administrador de Tareas ---------------- ")

      while True: 
       print("\n ------------- Menu ------------- ")
       print("\n 1.- Crear Usuario")
       print("\n 2.- Buscar Usuario")
       print("\n 3.- Eliminar Usuario")
       print("\n 4.- Marcar Tarea como Completada")

       print("\n 5.- Crear Tarea ")
       print("\n 6.- Buscar Tarea ")
       print("\n 7.- Eliminar Tarea")
       print("\n 8.- Eliminar Tareas de un Usuario")
       print("\n 9.- Obtener Tareas de el Usuario")
       print("\n 10.- Modificar Tarea ")
       print("\n 11.- Salir de Programa")

       eleccion = input("Que deseas hacer: ")

       match eleccion: 
           case 1: 
               print("Eleccion 1")
           case 2:
               print("Eleccion 2")
           case 3: 
               print("Eleccion 3")
           case 4: 
               print("Eleccion 4")
           case 5: 
               print("Eleccion 5")
           case 6:
               print("Eleccion 6")
           case 7: 
               print("Eleccion 7")
           case 8:
               print("Eleccion 8")
           case 9: 
               print("Eleccion 9")
           case 10: 
               print("Eleccion 10")
           case 11: 
               print("Saliste del programa, que tengas buen día (: ")
               print("Eleccion 11")
           
       





      