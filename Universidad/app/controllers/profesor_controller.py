from flask import Blueprint, request, jsonify
from app.models.profesor import Profesor

profesor_bp = Blueprint('profesor_bp', __name__)

@profesor_bp.route('/profesores', methods=['POST'])
def crear_profesor():
  data = request.get_json()
  profesor = Profesor(
    apellido=data['apellido'],
    nombre=data['nombre'],
    dni=data['dni'],
    sexo=data['sexo'],
    direccion=data['direccion'],
    anio_nacimiento=data['anio_nacimiento'],
    nacionalidad=data['nacionalidad'],
    titulo=data['titulo'],
    anio_egresado=data['anio_egresado'],
    anio_ingreso=data['anio_ingreso']
  )
  # Aquí se debería agregar la lógica para guardar el profesor en la base de datos
  return jsonify(profesor.__repr__()), 201

@profesor_bp.route('/profesores', methods=['GET'])
def obtener_profesores():
  # Aquí se debería agregar la lógica para obtener los profesores de la base de datos
  profesores = []  # Lista de profesores obtenidos de la base de datos
  return jsonify([profesor.__repr__() for profesor in profesores]), 200