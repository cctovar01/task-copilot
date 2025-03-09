from flask import Blueprint, request, jsonify
from app.models.materia import Materia
from app.models.periodo import Periodo

materia_bp = Blueprint('materia_bp', __name__)

@materia_bp.route('/materias', methods=['POST'])
def crear_materia():
  data = request.get_json()
  periodo = Periodo(data['periodo']['nombre'], data['periodo']['tiempo'])
  materia = Materia(
    nombre=data['nombre'],
    codigo=data['codigo'],
    creditos=data['creditos'],
    periodo=periodo
  )
  # Aquí se debería agregar la lógica para guardar la materia en la base de datos
  return jsonify(materia.__repr__()), 201

@materia_bp.route('/materias', methods=['GET'])
def obtener_materias():
  # Aquí se debería agregar la lógica para obtener las materias de la base de datos
  materias = []  # Lista de materias obtenidas de la base de datos
  return jsonify([materia.__repr__() for materia in materias]), 200