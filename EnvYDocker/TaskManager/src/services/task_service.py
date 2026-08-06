"""
from dataclasses import dataclass, field 
from datetime import datetime
from src.models import Tarea, Usuario
from src.utils.validatorsYutils import  verficar_existencia_usuario, verificar_fecha, creador_fecha

@dataclass
class Task_Service: 

  __listaUsuarios : list[Usuario] = field(default_factory=list)
  __listaTareas : list[Tarea] = field(default_factory=list)

  @property
  def listaUsuarios(self) -> list: 
    return self.__listaUsuarios

  @property 
  def listaTareas(self) -> list:
    return self.__listaTareas

  def crearTarea(self, UsuarioParam): 

    print("\n --------------------- Creador de Tareas --------------------- ")
    nombre = input("Por favor dame el nombre de tu tarea: ")

    fechaLimite = creador_fecha()

    self.__listaTareas.append(Tarea(nombre, fechaLimite, UsuarioParam))
   


  def crearUsuario(self):
      nombre = input("Dame tu nombre por favor: ")
      correo = input("Ahora Dame tu correo por favor(formato = nombre@email.com): ")

      self.__listaUsuarios.append(Usuario(nombre, correo))

  def buscarUsuario(self, nombreUsuario):

      for Usuario in self.__listaUsuarios:
         if Usuario.nombre == nombreUsuario: 
            return Usuario

      raise TypeError("\nEl usuario que buscas no Existe")

  def buscarTarea(self, nombreTarea):
  
     for Tarea in self.__listaTareas:
           if Tarea.nombre == nombreTarea: 
              return Tarea
  
     raise TypeError("\La Tarea que buscas no Existe")

  def eliminarUsuario(self, nombreUsuario): 
      for Usuario in self.__listaUsuarios:
               if Usuario.nombre == nombreUsuario: 
                  UsuarioAux = Usuario
                  self.listaUsuarios.remove(Usuario)
                  return UsuarioAux
               
      raise TypeError("\nEl usuario que buscas eliminar no Existe")

  def eliminarTarea(self, nombreTarea): 
    
      for Tarea in self._listaUsuarios:
        if Tarea.nombre == nombreTarea:  
          TareaAux = Tarea
          self.__listaTareas.remove(Tarea)
          return TareaAux

      raise TypeError("\nLa Tarea que buscas eliminar no Existe")

  def eliminarTareasUsuario(self, nombreUsuario): 
     for Tarea in self._listaTareas: 
       if Tarea.perteneceAUsuario.nombre == nombreUsuario: 
           self.__listaTareas.remove(Tarea)

  def obtenerTareasUsuario(self, nombreUsuario): 
      listaTareasUsuario = []
      for Tarea in self._listaTareas: 
        if Tarea.perteneceAUsuario.nombre == nombreUsuario: 
           listaTareasUsuario.append(Tarea)
      return listaTareasUsuario

  def modificarTarea(self, Tarea, atributo):
     
     if not isinstance(atributo, int):
        raise TypeError("El valor del atributo no coincide con ninguno de la Tarea")

     match atributo: 
        case 1: 
           Tarea.nombre(input("Dame el nombre nuevo de tu tarea"))
        case 2: 
           Tarea.fechaCreacion(creador_fecha())
        case 3: 
           Tarea.fechaLimite(creador_fecha())
        case 4: 
           Usuario = input("Dame el nombre del usuario al que deseas agregarle La tarea Nueva: ")
           Tarea.perteneAUsuario(self.buscarUsuario(Usuario))
        case 5:
           if Tarea.estatus: 
             Tarea.estatus(False)
           else: 
              self.tareaCompletada(Tarea)
     

  def tareaCompletada(self,Tarea):
     Tarea.estatus(True)
"""