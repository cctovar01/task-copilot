from flask import Blueprint, request, jsonify
from app.models.estudiante import Estudiante

estudiante_bp = Blueprint('estudiante_bp', __name__)

@estudiante_bp.route('/estudiantes', methods=['POST'])
def crear_estudiante():
  data = request.get_json()
  estudiante = Estudiante(
    apellido=data['apellido'],
    nombre=data['nombre'],
    dni=data['dni'],
    sexo=data['sexo'],
    direccion=data['direccion'],
    anio_nacimiento=data['anio_nacimiento'],
    nacionalidad=data['nacionalidad'],
    anio_ingreso=data['anio_ingreso']
  )
  # Aquí se debería agregar la lógica para guardar el estudiante en la base de datos
  return jsonify(estudiante.__repr__()), 201

@estudiante_bp.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
  # Aquí se debería agregar la lógica para obtener los estudiantes de la base de datos
  estudiantes = []  # Lista de estudiantes obtenidos de la base de datos
  return jsonify([estudiante.__repr__() for estudiante in estudiantes]), 200