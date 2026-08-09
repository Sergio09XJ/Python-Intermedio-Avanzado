from src.models.Tarea import Tarea 
from src.models.Usuario import Usuario
from src.services.Task_Service import Task_Service 
from datetime import datetime


def test_crear_usuario():
   usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   assert usuarioPrueba.__post_init__() == True

def test_crear_usuario_error():
   usuarioPrueba = Usuario(234, True)
   assert usuarioPrueba.__post_init__() == False

def test_crear_tarea():
   usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea = Tarea("Estudiar Ec.Dif.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
   assert usuarioTarea.__post_init__() == True

def test_crear_tarea_error():
    usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
    usuarioTarea = Tarea(234234, datetime(26, 8, 30, 15, 30), usuarioPrueba)
    assert usuarioTarea.__post_init__() == False


def test_completar_tarea(): 

   usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea = Tarea("Estudiar Ec. Dif.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea.estatus == True
   assert usuarioTarea.estatus == True

def test_modificar_tarea_Nombre(): 

   usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea = Tarea("Estudiar Ec. Dif.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea.name = "Aideé Santana"
   assert usuarioTarea.nombre ==  "Aideé Santana"

def test_modificar_tarea_fechaCreación(): 
   usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea = Tarea("Estudiar Ec. Dif.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea.fechaCreacion = datetime(26, 8, 8, 16, 00)
   assert usuarioTarea.fechaCreacion ==  datetime(26, 8, 8, 16, 00)

def test_modificar_tarea_fechaLimite(): 

   usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea = Tarea("Estudiar Ec. Dif.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea.fechaLimite = datetime(26, 8, 31, 18, 25)
   assert usuarioTarea.fechaLimite ==  datetime(26, 8, 31, 18, 25)

def test_modificar_tarea_Nombre_con_Service(): 
   administrador_tareas = Task_Service()
   usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea = Tarea("Estudiar Ec. Dif.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
   administrador_tareas.modficarTarea(usuarioTarea, 1)
   assert usuarioTarea.nombre ==  "Aideé Santana"

def test_modificar_tarea_fechaCreación_con_Service(): 
   administrador_tareas = Task_Service()
   usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea = Tarea("Estudiar Ec. Dif.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
   administrador_tareas.modficarTarea(usuarioTarea, 2)
   assert usuarioTarea.fechaCreacion ==  datetime(26, 8, 8, 16, 00)

def test_modificar_tarea_fechaLimite_con_Service(): 
   administrador_tareas = Task_Service()
   usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea = Tarea("Estudiar Ec. Dif.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
   administrador_tareas.modficarTarea(usuarioTarea, 3)
   assert usuarioTarea.__fechaLimite ==  datetime(26, 8, 31, 18, 25)

def test_completar_tarea_con_service():

   administrador_tareas = Task_Service()
   usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea_1 = Tarea("Estudiar Ec. Dif.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea_2 = Tarea("Estudiar Alg. Lin.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea_3 = Tarea("Estudiar Proba.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea_4 = Tarea("Estudiar C++.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
   
   administrador_tareas.agregarTarea(usuarioTarea_1)
   administrador_tareas.agregarTarea(usuarioTarea_2)
   administrador_tareas.agregarTarea(usuarioTarea_3)
   administrador_tareas.agregarTarea(usuarioTarea_4)
     
   administrador_tareas.tareaCompletada(usuarioTarea_1)
   assert usuarioTarea_1.estatus == True

def test_agregar_tarea():

   administrador_tareas = Task_Service()
   usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea = Tarea("Estudiar Ec. Dif.", datetime(26, 8, 30, 15, 30), usuarioPrueba)

   administrador_tareas.agregarTarea(usuarioTarea)
   assert administrador_tareas.listaTareas[-1] == usuarioTarea

def test_agregarUsuario():

   administrador_tareas = Task_Service()
   usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")

   administrador_tareas.agregarUsuario(usuarioPrueba)
   assert administrador_tareas.listaUsuarios[-1] == usuarioPrueba

def test_eliminar_tarea():

   administrador_tareas = Task_Service()
   usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea_1 = Tarea("Estudiar Ec. Dif.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea_2 = Tarea("Estudiar Alg. Lin.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea_3 = Tarea("Estudiar Proba.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea_4 = Tarea("Estudiar C++.", datetime(26, 8, 30, 15, 30), usuarioPrueba)

   administrador_tareas.agregarTarea(usuarioTarea_1)
   administrador_tareas.agregarTarea(usuarioTarea_2)
   administrador_tareas.agregarTarea(usuarioTarea_3)
   administrador_tareas.agregarTarea(usuarioTarea_4)

   assert administrador_tareas.eliminarTarea("Estudiar Ec. Dif.") == usuarioTarea_1

def test_buscar_tarea():

  administrador_tareas = Task_Service()
  usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
  usuarioTarea_1 = Tarea("Estudiar Ec. Dif.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
  usuarioTarea_2 = Tarea("Estudiar Alg. Lin.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
  usuarioTarea_3 = Tarea("Estudiar Proba.", datetime(26, 8, 30, 15, 30), usuarioPrueba)
  usuarioTarea_4 = Tarea("Estudiar C++.", datetime(26, 8, 30, 15, 30), usuarioPrueba)

  administrador_tareas.agregarTarea(usuarioTarea_1)
  administrador_tareas.agregarTarea(usuarioTarea_2)
  administrador_tareas.agregarTarea(usuarioTarea_3)
  administrador_tareas.agregarTarea(usuarioTarea_4)
  
  assert administrador_tareas.buscarTarea("Estudiar Ec. Dif.") == usuarioTarea_1


   
   
   
