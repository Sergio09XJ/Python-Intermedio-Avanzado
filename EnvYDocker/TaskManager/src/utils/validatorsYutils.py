import re
import random
from datetime import datetime
from src.models.Usuario import Usuario
from src.services.Task_Service import Task_Service


def verificar_iD(iD : int) -> bool:
  if not isinstance(iD, int) or ( iD < 100000 or iD > 999999): 
    return False
  return True

def verificar_nombre(nombre : str) -> bool:
  if not isinstance(nombre, str): 
    return False
  return True

def verificar_correo(correo : str) -> bool:
  if isinstance(correo, str):
    patronCorreo = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.fullmatch(patronCorreo, correo) is not None
  return False
   

def verificar_fecha(laFecha : datetime) -> bool:
  ahora = datetime.now().replace(second=0, microsecond=0)
  if not isinstance(laFecha, datetime) or laFecha < ahora:
    return False
  return True

def verficar_existencia_usuario(nombreBuscar : str, taskService : Task_Service) -> bool:

  for  Usuario in taskService.listaUsuarios: 
    if Usuario.name == nombreBuscar:
      return True
  return False

def verificar_estatus(estatus : bool) -> bool:
  if not isinstance(estatus, bool):
     return False
  return True

def verificar_usuario(UsuarioAVerficiar : Usuario) -> bool: 
  if not isinstance(UsuarioAVerficiar, Usuario):
    return False
  return True

def genAleatorio() -> int:
  return random.randint(10000, 999999)

def creador_fecha() -> datetime:
  inputF = input("Ahora dame la fecha Limite - ejemplo: 26/09/12/13/30 | Los ultimos 2 dijitos corresponden a la hora(formato de 24 hrs) y minuto ")
  listaInput = inputF.split("/")
  return datetime(int(listaInput[0]), int(listaInput[1]), int(listaInput[2]), int(listaInput[3]), int(listaInput[4]))
  