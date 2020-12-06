from bd import inicializar_bd
from entrypoints import flask_app
from service_layer.controlador_bot import ControladorBot


Session = inicializar_bd()

# CONTROLADOR_BOT = ControladorBot()

# flask_app.APP.run()


















# funciona perfecto
# charla = Charla("inactiva", "3", "4", "5", "6")
# charla.logs.append(Log(3, "43", False, "hola", "123", "1", "nuevo"))
# session.add(charla)
# session.commit()

import profilex



# funciona bien. update
# parametro=session.query(Parametro).first()
# parametro.maximo_intentos_fallidos=4
# session.commit()


# print("camello:",r.camello)
# print("logs")

# for x in session.query(Log):
#     print(x)
#     print(x.id_charla)
#     print(x.charla)


# session.add(charla)
# session.commit()





# buena forma de agregar muchos a la vez,
# hacer una tupla
# # create catalog
# tshirt, mug, hat, crowbar = (
#     Charla("inactiva", "3", "4", "5", "6"),
#     Charla("inactiva", "3", "4", "5", "6"),
#     Charla("inactiva", "3", "4", "5", "6"),
#     Charla("inactiva", "3", "4", "5", "6"),
# )
# session.bulk_save_objects([tshirt, mug, hat, crowbar])
# with profilex.profiled():
#     session.commit()
