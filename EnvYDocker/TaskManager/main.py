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
      administradorTareas = Task_Service()
      print("\n ---------------- Administrador de Tareas ---------------- ")

      while True: 
       print("\n             ------------- Menu ------------- ")
       print("\n1.- Crear Usuario | 2.- Buscar Usuario")
       print("3.- Eliminar Usuario | 4.- Marcar Tarea como Completada")
       print("5.- Crear Tarea | 6.- Buscar Tarea")
       print("7.- Eliminar Tarea | 8.- Eliminar Tareas de un Usuario")
       print("9.- Obtener Tareas de el Usuario | 10.- Modificar Tarea | 11.- Salir de Programa ")

       eleccion = input("Que deseas hacer: ")

       match eleccion: 
           case "1": 
               print("Eleccion 1")
               administradorTareas.crearUsuario()
           case "2":
               print("Eleccion 2")
               administradorTareas.crearTarea()
           case "3": 
               print("Eleccion 3")
               administradorTareas.eliminarTarea()
           case "4": 
               print("Eleccion 4")
               try:
                 TareaACompletar = input("Dame el nombre tarea que deseas buscar: ")
                 administradorTareas.tareaCompletada(administradorTareas.buscarTarea(TareaACompletar))
               except ValueError as e:
                   print(f"{e}")        
           case "5": 
               print("Eleccion 5")
               try: 
                TareaACompletar = input("Dame el nombre tarea que deseas buscar: ")
                administradorTareas.buscarTarea(TareaACompletar).mostrarTarea()
               except ValueError as e:
                 print(f"{e}")    
           case "6":
               print("Eleccion 6")
               try: 
                TareaABuscar = input("\n Dame el nombre de la tarea que deseas buscar: ")
                administradorTareas.buscarTarea(TareaABuscar).mostrarTarea()
               except ValueError as e: 
                print(f"{e}")
           case "7": 
               print("Eleccion 7")
               try: 
                 TareaAEliminar = input("\nDame el nombre de la Tarea que desesas buscar: ")
                 administradorTareas.eliminarTarea(TareaAEliminar)
               except ValueError as e: 
                 print(f"{e}")
           case "8":
               print("Eleccion 8")
               try: 
                UsuarioAEliminarTareas = input("\n Dame el nombre del usuario para eliminar sus tareas: ")
                Tareas = administradorTareas.eliminarTareasUsuario(UsuarioAEliminarTareas)
                print("\nLa lista de tareas eliminadas es: ")
                for Tarea in Tareas: 
                  print("\n")
                  Tarea.mostrarTarea()
               except ValueError as e: 
                  print(f"{e}")
                  
           case "9": 
               print("Eleccion 9")
               try: 
                 UsuarioAEliminarTareas = input("\n Dame el nombre del usuario para eliminar sus tareas: ")
                 Tareas = administradorTareas.obtenerTareasUsuario(UsuarioAEliminarTareas)
                 print("\nLa lista de tareas eliminadas es: ")
                 for Tarea in Tareas: 
                     print("\n")
                     Tarea.mostrarTarea()
               except ValueError as e: 
                  print(f"{e}")
           case "10": 
               print("Eleccion 10")
               try: 
                UsuarioAEliminarTareas = input("\n Dame el nombre del usuario para eliminar sus tareas: ")
                Tareas = administradorTareas.obtenerTareasUsuario(UsuarioAEliminarTareas)
                print("\nLa lista de tareas eliminadas es: ")
                 for Tarea in Tareas: 
                  print("\n")
                 Tarea.mostrarTarea()
               except ValueError as e: 
                print(f"{e}")
           case "11": 
               print("Saliste del programa, que tengas buen día (: ")
         
               break
           case _:
               print("\nElección invalidad, no puedes poner valores diferentes a los del menu. ")
           
       


main()


      