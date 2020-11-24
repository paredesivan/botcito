from controladorBot import ControladorBot
from flask import Flask, request
from flask_cors import CORS
import jsonify
import orm
from sqlalchemy import create_engine, connectors
from sqlalchemy.orm import sessionmaker
from orm import metadata, start_mappers
from movil import Movil


APP = Flask(__name__)
CORS(APP)

CONTROLADOR_BOT = ControladorBot()

engine = create_engine('postgres://mzmqoonm:xhZeUWN5TPvYKQYAQdCelh2SSx2Wpjas@suleiman.db.elephantsql.com:5432/mzmqoonm')
Session = sessionmaker(bind=engine)
session = Session()

orm.start_mappers()  # similar a crear schema supongo


@APP.route('/nuevo_mensaje', methods=['POST'])
def nuevo_mensaje():
    # al request-data se lo tengo que pasar limpio
    rta = CONTROLADOR_BOT.nuevo_mensaje(request.data)
    print(rta)
    # return parseador.codificar(rta)\


@APP.route('/finalizar_charla', methods=['POST'])
def finalizar_charla():
    rta = CONTROLADOR_BOT.finalizar_charla(request.data)
    print(rta)

    # return parseador.codificar(rta)


if __name__ == '__main__':
    APP.run()
