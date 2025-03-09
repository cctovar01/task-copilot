class Persona:
  def __init__(self, apellido, nombre, dni, sexo, direccion, anio_nacimiento, nacionalidad):
    self.apellido = apellido
    self.nombre = nombre
    self.dni = dni
    self.sexo = sexo
    self.direccion = direccion
    self.anio_nacimiento = anio_nacimiento
    self.nacionalidad = nacionalidad
  def __repr__(self):
    return f"<Persona {self.nombre} {self.apellido}>"