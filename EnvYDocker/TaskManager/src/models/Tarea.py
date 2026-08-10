
from dataclasses import dataclass
from datetime import datetime
from src.utils.validatorsYutils import verificar_fecha, verificar_nombre, verificar_estatus
from src.models.Usuario import Usuario, verificar_usuario



@dataclass
class Tarea: 

  __nombre : str
  __fechaLimite : datetime
  __perteneceAUsuario : Usuario
  __estatus = False
  __fechaCreacion = datetime.now().replace(second=0, microsecond=0)

  def __post_init__(self):
    if verificar_nombre(self.__nombre) == False: 
       raise TypeError("El nombre no es del tipo correcto. ")
    if verificar_fecha(self.__fechaCreacion) == False: 
           raise TypeError("El tipo de dato no coincide con el tipo de fecha de creación o esta fuera de los limites.")
    if verificar_fecha(self.__fechaLimite) == False: 
               raise TypeError("El tipo de dato no coincide con el tipo de fecha limite o esta fuera de los limites.")
    if verificar_estatus(self.__estatus) == False: 
           raise TypeError("El tipo de dato no es correcto para el estatus de la Tarea. ")
    if verificar_usuario(self.__perteneceAUsuario) == False: 
          raise TypeError("El tipo de dato no es del tipo Usuario") 
    return True
 

  @property
  def nombre(self) -> str: 
     return self.__nombre

  @nombre.setter
  def nombre(self, nuevoNombre : str) -> None: 
     if verificar_nombre(nuevoNombre) == True:
        self.__nombre = nuevoNombre
     else: 
        raise TypeError("El tipo de dato no es correcto para el nombre de la Tarea."); 

  @property
  def estatus(self) -> bool: 
     return self.__estatus 

  @estatus.setter
  def estatus(self, nuevoEstatus : bool) -> None: 
       if verificar_estatus(nuevoEstatus) == True:
          self.__estatus = nuevoEstatus
       else: 
          raise TypeError("El tipo de dato no es correcto para el estatus de la Tarea."); 

  @property 
  def fechaCreacion(self) -> datetime: 
     return self.__fechaCreacion

  @fechaCreacion.setter
  def fechaCreacion(self, nuevaFechaCreacion : datetime) -> None: 
       if verificar_fecha(nuevaFechaCreacion) == True:
          self.__fechaCreacion = nuevaFechaCreacion
       else: 
          raise TypeError("El tipo de dato no coincide con el tipo de fecha o esta fuera de los limites."); 

  @property
  def fechaLimite(self) -> datetime:
     return self.__fechaLimite

  @fechaLimite.setter
  def fechaLimite(self, nuevaFechaLimite : datetime) -> None: 
         if verificar_fecha(nuevaFechaLimite) == True:
            self.__fechaLimite = nuevaFechaLimite
         else: 
            raise TypeError("El tipo de dato no coincide con el tipo de fecha o esta fuera de los limites."); 

  @property
  def perteneceAUsuario(self) -> Usuario:
       return self.__perteneceAUsuario

  @perteneceAUsuario.setter
  def perteneceAUsuario(self, UsuarioNuevo : Usuario) -> None: 
         if verificar_usuario(UsuarioNuevo) == True:
              self.__perteneceAUsuario = UsuarioNuevo
         else: 
              raise TypeError("El tipo de dato no es booleano"); 

  def mostrarTarea(self) -> str:
      completada = "si" if self.__estatus else "no"
      return f"\nEl nombre de tu tarea es: {self.__nombre} \n La fecha Limite es: {self.__fechaLimite} \n La fecha de creación es: {self.__fechaCreacion} \n La Tarea pertenece al Usuario: {self.__perteneceAUsuario} \n La Tarea {completada} esta completada " 
    



 

 