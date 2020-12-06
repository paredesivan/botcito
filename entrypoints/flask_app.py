from flask import jsonify, Flask, request
from flask_cors import CORS
from service_layer.controlador_bot import ControladorBot
from bd import inicializar_bd
from hilos import ejecutar_tarea
from adapters.sql_repository_nodo import SqlRepositoryNodo
from domain.parametro import Parametro

sesion = inicializar_bd()
CONTROLADOR_BOT = ControladorBot(sesion)

APP = Flask(__name__)
CORS(APP)


# print(SqlRepositoryNodo(sesion).obtener_tags(1)[0].hijos[0].tags[0].texto)
# print(SqlRepositoryNodo(sesion).obtener_tags(1)[0].tags[0].texto)
# print(SqlRepositoryNodo(sesion).obtener_tags(1)[0].hijos[1].tags)
# print(SqlRepositoryNodo(sesion).obtener_tags(1)[0].hijos[2].tags)
# parametro=sesion.query(Parametro).first()
# print(parametro.obtener_maximo_intentos_fallidos())
# print(parametro.modo_del_parametro)
@APP.route('/nuevo_mensaje', methods=['POST'])
def nuevo_mensaje():
    # limpiar
    # procesar
    # devolver
    # al request-data se lo tengo que pasar limpio

    datos = request.json

    try:
        rta = CONTROLADOR_BOT.nuevo_mensaje(datos)
        return jsonify(rta['Dato']), 200
    except Exception as e:
        return jsonify({"falla": str(e)}), 400


    # return parseador.codificar(rta)\


def inicializar_tareas():
    pass
    # ejecutar_tarea(finalizar_charlas_viejas, (''), 600)
    # ejecutar_tarea(limpiar_tablas, (''), 600)


if __name__ == '__main__':
    APP.run()
    inicializar_tareas()
