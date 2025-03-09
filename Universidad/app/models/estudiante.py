from persona import Persona

class Estudiante(Persona):
  def __init__(self, apellido, nombre, dni, sexo, direccion, anio_nacimiento, nacionalidad, anio_ingreso):
    super().__init__(apellido, nombre, dni, sexo, direccion, anio_nacimiento, nacionalidad)
    self.anio_ingreso = anio_ingreso
  def __repr__(self):
    return f"<Estudiante {self.nombre} {self.apellido}, Año de Ingreso: {self.anio_ingreso}>"