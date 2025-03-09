from flask import Blueprint, request, jsonify
from app.models.periodo import Periodo

periodo_bp = Blueprint('periodo_bp', __name__)

@periodo_bp.route('/periodos', methods=['POST'])
def crear_periodo():
  data = request.get_json()
  periodo = Periodo(
    nombre=data['nombre'],
    tiempo=data['tiempo'],
    materias=data.get('materias', [])
  )
  # Aquí se debería agregar la lógica para guardar el periodo en la base de datos
  return jsonify(periodo.__repr__()), 201

@periodo_bp.route('/periodos', methods=['GET'])
def obtener_periodos():
  # Aquí se debería agregar la lógica para obtener los periodos de la base de datos
  periodos = []  # Lista de periodos obtenidos de la base de datos
  return jsonify([periodo.__repr__() for periodo in periodos]), 200