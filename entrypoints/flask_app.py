from flask import jsonify, Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from service_layer.controlador_bot import ControladorBot
from bd import inicializar_bd
from hilos import ejecutar_tarea
from adapters.sql_repository_nodo import SqlRepositoryNodo
from domain.parametro import Parametro


sesion = inicializar_bd()
CONTROLADOR_BOT = ControladorBot(sesion)

APP = Flask(__name__)
CORS(APP)

# esto es un agregado de flask restful, permite hacer get y post y chucherias
API=Api(APP)


# print(SqlRepositoryNodo(sesion).obtener_tags(1)[0].hijos[0].tags[0].texto)
# print(SqlRepositoryNodo(sesion).obtener_tags(1)[0].tags[0].texto)
# print(SqlRepositoryNodo(sesion).obtener_tags(1)[0].hijos[1].tags)
# print(SqlRepositoryNodo(sesion).obtener_tags(1)[0].hijos[2].tags)
# parametro=sesion.query(Parametro).first()
# print(parametro.obtener_maximo_intentos_fallidos())
# print(parametro.modo_del_parametro)


# API.add_resource
@APP.route('/tag', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def tag():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PATCH':
        pass
    if request.method == 'DELETE':
        pass


@APP.route('/nuevo_mensaje', methods=['POST'])
def nuevo_mensaje():
    # limpiar
    # procesar
    # devolver
    # al request-data se lo tengo que pasar limpio

    datos = request.json

    try:
        rta = CONTROLADOR_BOT.nuevo_mensaje(datos)
        return jsonify({"mensaje": rta['Dato']}), 200  # puedo devolver solo el 200
    except Exception as e:
        print(e)
        return jsonify({"mensaje": str(e)}), 400

    # return parseador.codificar(rta)\


def inicializar_tareas():
    pass
    # ejecutar_tarea(finalizar_charlas_viejas, (''), 600)
    # ejecutar_tarea(limpiar_tablas, (''), 600)
    # ejecutar_tarea(reenviar_mensajes_pendientes, (''), 20)


if __name__ == '__main__':
    APP.run()
    inicializar_tareas()
