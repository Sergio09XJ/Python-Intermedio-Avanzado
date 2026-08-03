import re
import random
from datetime import datetime
from src.models import Usuario

def verificar_iD(iD) -> bool:
  if not isinstance(iD, int) or ( iD < 100000 or iD > 999999): 
    return False
  return True

def verificar_nombre(nombre) -> bool:
  if not isinstance(nombre, str): 
    return False
  return True

def verificar_correo(correo) -> bool:
  if isinstance(correo, str):
    patronCorreo = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.fullmatch(patronCorreo, correo)
  return False
   

def verificar_fecha(laFecha) -> bool:
  ahora = datetime.now().replace(second=0, microsecond=0)
  if not isinstance(laFecha, datetime) or laFecha < ahora:
    return False
  return True

def verficar_existencia_usuario(nombreBuscar, taskService) -> bool:

  for  Usuario in taskService.listaUsuarios(): 
    if Usuario.name == nombreBuscar:
      return True
  return False

def verificar_estatus(estatus) -> bool:
  if not isinstance(estatus, bool):
     return False
  return True

def verificar_usuario(UsuarioAVerficiar) -> bool: 
  if not isinstance(UsuarioAVerficiar, Usuario):
    return False
  return True

def genAleatorio() -> int:
  return random.randint(10000, 999999)

def creador_fecha() -> datetime:
  inputF = input("Ahora dame la fecha Limite - ejemplo: 26/09/12/13/30 | Los ultimos 2 dijitos corresponden a la hora(formato de 24 hrs) y minuto ")
  inputF = inputF.split("/")
  return datetime(inputF[0], inputF[1], inputF[2], inputF[3], inputF[4])