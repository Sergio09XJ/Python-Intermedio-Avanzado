
from dataclasses import dataclass
from datatime import datatime
from src.utils import verificar_fecha, verificar_nombre, verificar_estatus, genAleatorio

class task: 

  __nombre : str
  __estatus : bool 
  __fechaCreacion : datatime 
  __fechaLimite : datatime