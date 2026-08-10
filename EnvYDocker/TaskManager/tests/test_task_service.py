from src.models.Tarea import Tarea 
from src.models.Usuario import Usuario
from src.services.Task_Service import Task_Service 
from datetime import datetime
import pytest


def test_crear_usuario():
   usuarioPrueba_0 = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   assert usuarioPrueba_0.__post_init__() == True


def test_crear_tarea():
   usuarioPrueba_1 = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea = Tarea("Estudiar Ec.Dif.", datetime(2026, 8, 30, 15, 30), usuarioPrueba_1)
   assert usuarioTarea.__post_init__() == True


def test_completar_tarea(): 

   usuarioPrueba_2 = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea = Tarea("Estudiar Ec. Dif.", datetime(2026, 8, 30, 15, 30), usuarioPrueba_2)
   usuarioTarea.estatus = True
   print(usuarioTarea.estatus)
   assert usuarioTarea.estatus == True


def test_modificar_tarea_Nombre(): 

   usuarioPrueba_3 = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea = Tarea("Estudiar Ec. Dif.", datetime(2026, 8, 30, 15, 30), usuarioPrueba_3)
   usuarioTarea.nombre = "Estudiar Teo. Grafos"
   assert usuarioTarea.nombre == "Estudiar Teo. Grafos"


def test_modificar_tarea_fechaCreación(): 
   usuarioPrueba_4 = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea = Tarea("Estudiar Ec. Dif.", datetime(2026, 8, 30, 15, 30), usuarioPrueba_4)
   usuarioTarea.fechaCreacion = datetime(2026, 8, 10, 16, 00)
   assert usuarioTarea.fechaCreacion ==  datetime(2026, 8, 10, 16, 00)


def test_modificar_tarea_fechaLimite(): 

   usuarioPrueba_5 = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea = Tarea("Estudiar Ec. Dif.", datetime(2026, 8, 30, 15, 30), usuarioPrueba_5)
   usuarioTarea.fechaLimite = datetime(2026, 8, 31, 18, 25)
   assert usuarioTarea.fechaLimite ==  datetime(2026, 8, 31, 18, 25)


def test_completar_tarea_con_service():

   administrador_tareas = Task_Service()
   usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea_1 = Tarea("Estudiar Ec. Dif.", datetime(2026, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea_2 = Tarea("Estudiar Alg. Lin.", datetime(2026, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea_3 = Tarea("Estudiar Proba.", datetime(2026, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea_4 = Tarea("Estudiar C++.", datetime(2026, 8, 30, 15, 30), usuarioPrueba)
   
   administrador_tareas.agregarTarea(usuarioTarea_1)
   administrador_tareas.agregarTarea(usuarioTarea_2)
   administrador_tareas.agregarTarea(usuarioTarea_3)
   administrador_tareas.agregarTarea(usuarioTarea_4)
     
   administrador_tareas.tareaCompletada(usuarioTarea_1)
   assert usuarioTarea_1.estatus == True

def test_agregar_tarea():

   administrador_tareas = Task_Service()
   usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
   usuarioTarea = Tarea("Estudiar Ec. Dif.", datetime(2026, 8, 30, 15, 30), usuarioPrueba)

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
   usuarioTarea_1 = Tarea("Estudiar Ec. Dif.", datetime(2026, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea_2 = Tarea("Estudiar Alg. Lin.", datetime(2026, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea_3 = Tarea("Estudiar Proba.", datetime(2026, 8, 30, 15, 30), usuarioPrueba)
   usuarioTarea_4 = Tarea("Estudiar C++.", datetime(2026, 8, 30, 15, 30), usuarioPrueba)

   administrador_tareas.agregarTarea(usuarioTarea_1)
   administrador_tareas.agregarTarea(usuarioTarea_2)
   administrador_tareas.agregarTarea(usuarioTarea_3)
   administrador_tareas.agregarTarea(usuarioTarea_4)

   assert administrador_tareas.eliminarTarea("Estudiar Ec. Dif.") == usuarioTarea_1

def test_buscar_tarea():

  administrador_tareas = Task_Service()
  usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
  usuarioTarea_1 = Tarea("Estudiar Ec. Dif.", datetime(2026, 8, 30, 15, 30), usuarioPrueba)
  usuarioTarea_2 = Tarea("Estudiar Alg. Lin.", datetime(2026, 8, 30, 15, 30), usuarioPrueba)
  usuarioTarea_3 = Tarea("Estudiar Proba.", datetime(2026, 8, 30, 15, 30), usuarioPrueba)
  usuarioTarea_4 = Tarea("Estudiar C++.", datetime(2026, 8, 30, 15, 30), usuarioPrueba)

  administrador_tareas.agregarTarea(usuarioTarea_1)
  administrador_tareas.agregarTarea(usuarioTarea_2)
  administrador_tareas.agregarTarea(usuarioTarea_3)
  administrador_tareas.agregarTarea(usuarioTarea_4)
  
  assert administrador_tareas.buscarTarea("Estudiar Ec. Dif.") == usuarioTarea_1


def test_crear_usuario_error():
   with pytest.raises(TypeError, match="El nombre no es del tipo correcto. "):
       usuarioPrueba_7 = Usuario(234, "sergiodanielac9@gmail.com")


def test_crear_tarea_error():
    with pytest.raises(TypeError, match="El tipo de dato no coincide con el tipo de fecha limite o esta fuera de los limites."):
     usuarioPrueba = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
     usuarioTarea = Tarea("Hacer Horario", datetime(26, 8, 30, 15, 30), usuarioPrueba)


def test_modificar_tarea_Nombre_con_Service(monkeypatch):

    administrador_tareas = Task_Service()
    usuarioPrueba_8 = Usuario("Sergio Daniel", "sergiodaniel@gmail.com")
    usuarioTarea = Tarea( "Estudiar Ec. Dif.", datetime(2026, 8, 30, 15, 30), usuarioPrueba_8)
    monkeypatch.setattr("builtins.input", lambda _: "Programación")
    administrador_tareas.modificarTarea(usuarioTarea, "1")
    assert usuarioTarea.nombre == "Programación"