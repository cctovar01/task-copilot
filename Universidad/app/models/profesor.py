from persona import Persona

class Profesor(Persona):
  def __init__(self, apellido, nombre, dni, sexo, direccion, anio_nacimiento, nacionalidad, titulo, anio_egresado, anio_ingreso):
    super().__init__(apellido, nombre, dni, sexo, direccion, anio_nacimiento, nacionalidad)
    self.titulo = titulo
    self.anio_egresado = anio_egresado
    self.anio_ingreso = anio_ingreso

  def __repr__(self):
    return f"<Profesor {self.nombre} {self.apellido}, Título: {self.titulo}, Año de Egresado: {self.anio_egresado}, Año de Ingreso: {self.anio_ingreso}>"