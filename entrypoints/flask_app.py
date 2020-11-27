import jsonify

from flask import Flask, request
from flask_cors import CORS
from main import CONTROLADOR_BOT

APP = Flask(__name__)
CORS(APP)


@APP.route('/nuevo_mensaje', methods=['POST'])
def nuevo_mensaje():
    # limpiar
    # procesar
    # devolver

    # al request-data se lo tengo que pasar limpio
    rta = CONTROLADOR_BOT.nuevo_mensaje(request.data)
    print(rta)
    # return parseador.codificar(rta)\


@APP.route('/estado_servicio', methods=['POST'])
def estado_servicio():
    # limpiar
    # procesar
    # devolver

    rta = CONTROLADOR_BOT.estado_servicio(request.data)
    print(rta)

    # return parseador.codificar(rta)


if __name__ == '__main__':
    APP.run()
