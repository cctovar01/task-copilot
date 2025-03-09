from app.models.periodo import Periodo

class Materia(Periodo):
  def __init__(self, nombre, codigo, creditos, periodo):
    super().__init__(periodo.nombre, periodo.tiempo, periodo.materias)
    self.nombre = nombre
    self.codigo = codigo
    self.creditos = creditos
    periodo.agregar_materia(self)

  def __repr__(self):
    return f"<Materia {self.nombre}, Código: {self.codigo}, Créditos: {self.creditos}>"