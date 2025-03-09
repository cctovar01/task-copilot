class Periodo:
  def __init__(self, nombre, tiempo, materias=None):
    self.nombre = nombre
    self.tiempo = tiempo
    self.materias = materias if materias is not None else []
  
  def agregar_materia(self, materia):
    self.materias.append(materia)
  
  def __repr__(self):
    return f"<Periodo {self.nombre}, Tiempo: {self.tiempo}, Materias: {len(self.materias)}>"