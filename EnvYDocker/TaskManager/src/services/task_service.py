
from dataclasses import dataclass, field 
from datetime import datetime
from src.models.Usuario import Usuario
from src.models.Tarea import Tarea
from src.utils.validatorsYutils import  creador_fecha

import logging

logger = logging.getLogger(__name__)

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


  def crearTarea(self, UsuarioParam : Usuario) -> Tarea: 


    nombre = input("\nPor favor dame el nombre de tu tarea: ")

    fechaLimite = creador_fecha()
    try: 
       self.__listaTareas.append(Tarea(nombre, fechaLimite, UsuarioParam))
       logger.info(f"La Tarea {nombre} se creo de forma correcta. ")
       return self.__listaTareas[-1]
    except TypeError: 
       logger.warning("No se pudo completar la creación de la tarea")
       raise 
   
   


  def crearUsuario(self) -> None:
      nombre = input("\nDame tu nombre por favor: ")
      correo = input("Ahora Dame tu correo por favor(formato = nombre@email.com): ")
      try: 
        self.__listaUsuarios.append(Usuario(nombre, correo))
        logger.info(f"El Usuario {nombre} se creo de forma correcta. ")
      except TypeError: 
         logger.warning("La craeción del usuario no se pudo completar.")
         raise


  def buscarUsuario(self, nombreUsuario : str) -> Usuario:

      for Usuario in self.__listaUsuarios:
         if Usuario.nombre == nombreUsuario:
            logger.info(f"El Usuario {nombreUsuario} se encontro correctamente") 
            return Usuario

      logger.warning("\nEl usuario que buscas no Existe")
      raise 

  def buscarTarea(self, nombreTarea : str) -> Tarea:
  
     for Tarea in self.__listaTareas:
           if Tarea.nombre == nombreTarea: 
              logger.info(f"La tarea {nombreTarea} se encontro correctamente. ")
              return Tarea
     logger.warning("\nLa Tarea que buscas no Existe")
     raise 

  def eliminarUsuario(self, nombreUsuario : str) -> Usuario: 
      for Usuario in self.__listaUsuarios:
               if Usuario.nombre == nombreUsuario: 
                  UsuarioAux = Usuario
                  self.listaUsuarios.remove(Usuario)
                  logger.info(f"El usuario {nombreUsuario} se elimino de forma correcta.")
                  return UsuarioAux
      logger.warning("\nEl usuario que buscas eliminar no Existe")
      raise

  def eliminarTarea(self, nombreTarea : str) -> Tarea: 
      
        for Tarea in self.__listaTareas:
          if Tarea.nombre == nombreTarea:  
            TareaAux = Tarea
            self.__listaTareas.remove(Tarea)
            logger.info(f"La tarea {nombreTarea} se elimino de forma correcta.")
            return TareaAux
  
        logger.warning("\nLa Tarea que buscas eliminar no Existe")
        raise 

  def agregarUsuario(self, UsuarioNuevo : Usuario ) -> None: 
       try: 
         self.__listaUsuarios.append(UsuarioNuevo)
         logger.info("Se agrego el usuario con exito. ")
       except: 
          logger.error("No se pudo agregar el usuario.")
          raise 
       
  def agregarTarea(self, TareaNueva : Tarea ) -> None: 
     try: 
       self.__listaTareas.append(TareaNueva)
       logger.info("Se agrego la tarea con exito. ")
     except: 
        logger.error("No se pudo agregar la tarea.")
        raise 
               

  def eliminarTareasUsuario(self, nombreUsuario : str) -> list[Tarea]: 
     for Tarea in self.__listaTareas: 
       if Tarea.perteneceAUsuario.nombre == nombreUsuario: 
           self.__listaTareas.remove(Tarea)
           logger.info(f"La tarea del Usuario {nombreUsuario} se elimino correctamente.")

     logger.warning(f"\nLa Tarea que buscas eliminar de {nombreUsuario} no Existe")
     raise 

  def obtenerTareasUsuario(self, nombreUsuario : str) -> list[Tarea]: 
      listaTareasUsuario = []
      for Tarea in self.__listaTareas: 
        if Tarea.perteneceAUsuario.nombre == nombreUsuario: 
           listaTareasUsuario.append(Tarea)
      logger.info(f"La tarea del Usuario {nombreUsuario} se retorna de forma correcta.")
      return listaTareasUsuario
  

  def modificarTarea(self, Tarea : Tarea, elector : str) -> None:
     
     if not isinstance(elector, str):
        logger.warning("El valor del atributo no coincide con ninguno de la Tarea")
        raise 

     match elector: 
        case "1": 
           Tarea.nombre = input("Dame el nombre nuevo de tu tarea")
           logger.info("Se modifico el nombre de tu Tarea.")
        case "2": 
           Tarea.fechaCreacion = creador_fecha() 
           logger.info("Se modifico la fecha de creación de tu Tarea.")
        case "3": 
           Tarea.fechaLimite = creador_fecha()
           logger.info("Se modifico la fehca limite de tu tarea.")
        case "4": 
           Usuario = input("Dame el nombre del usuario al que deseas agregarle La tarea Nueva: ")
           Tarea.perteneceAUsuario = self.buscarUsuario(Usuario)
           logger.info("Se modifico el dueño de la tarea.")
        case "5":
           if Tarea.estatus: 
             Tarea.estatus = False
             logger.info("Se marco como incompleta la tarea.")
           else: 
              self.tareaCompletada(Tarea)
        case _ :
           print("Tu elección no esta dentro de los parametros. ")
     

  def tareaCompletada(self,Tarea : Tarea) -> None:
     
     Tarea.estatus = True
     logger.info("Se marco como completada la tarea.")
