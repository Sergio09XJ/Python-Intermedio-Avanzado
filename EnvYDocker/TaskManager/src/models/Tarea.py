
from dataclasses import dataclass
from datetime import datetime
from src.utils import verificar_fecha, verificar_nombre, verificar_estatus, verificar_usuario
from src.models import Usuario
from typing import Optional

@dataclass
class Tarea: 

  __nombre : str
  __fechaLimite : datetime
  __perteneceAUsuario : Usuario
  __estatus : Optional[bool] = None 
  __fechaCreacion = datetime.now().replace(second=0, microsecond=0)

  def __post_init__(self):
    if verificar_nombre(self.__nombre) == False: 
       raise TypeError("El nombre no es del tipo correcto. ")
    if verificar_fecha(self.__fechaCreacion) == True: 
           raise TypeError("El tipo de dato no coincide con el tipo de fecha o esta fuera de los limites.")
    if verificar_fecha(self.__fechaLimite) == True: 
               raise TypeError("El tipo de dato no coincide con el tipo de fecha o esta fuera de los limites.")
    if verificar_estatus(self.__estatus) == False: 
           raise TypeError("El tipo de dato no es correcto para el estatus de la Tarea. ")
    if verificar_usuario(self.__perteneceAUsuario) == False: 
          raise TypeError("El tipo de dato no es del tipo Usuario") 
    return True
 

  @property
  def nombre(self) -> str: 
     return self.__nombre

  @property
  def estatus(self) -> bool: 
     return self.__estatus 

  @property 
  def fechaCreacion(self) -> datetime: 
     return self.__fechaCreacion

  @property
  def fechaLimite(self) -> datetime:
     return self.__fechaLimite

  @property
  def perteneceAUsuario(self) -> Usuario:
       return self.__perteneceAUsuario

  @nombre.getter
  def __perteneceAUsuario(self, nuevoNombre): 
     if verificar_nombre(nuevoNombre) == True:
        self.__nombre = nuevoNombre
     else: 
        raise TypeError("El tipo de dato no es correcto para el nombre de la Tarea."); 

  @estatus.getter
  def estatus(self, nuevoEstatus): 
       if verificar_estatus(nuevoEstatus) == True:
          self.__estatus = nuevoEstatus
       else: 
          raise TypeError("El tipo de dato no es correcto para el estatus de la Tarea."); 

  @fechaCreacion.getter
  def fechaCreacion(self, nuevaFechaCreacion): 
       if verificar_fecha(nuevaFechaCreacion) == True:
          self.fechaCreacion = nuevaFechaCreacion
       else: 
          raise TypeError("El tipo de dato no coincide con el tipo de fecha o esta fuera de los limites."); 

  @fechaLimite.getter
  def fechaLimite(self, nuevaFechaLimite): 
       if verificar_fecha(nuevaFechaLimite) == True:
          self.fechaLimite = nuevaFechaLimite
       else: 
          raise TypeError("El tipo de dato no coincide con el tipo de fecha o esta fuera de los limites."); 

  @estatus.getter
  def estatus(self, nuevoEstatus): 
       if verificar_usuario(nuevoEstatus) == True:
            self.__estatus = nuevoEstatus
       else: 
            raise TypeError("El tipo de dato no es booleano"); 
