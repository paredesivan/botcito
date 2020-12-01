from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from adapters.orm import start_mappers, metadata
from domain.parametro import Parametro
from domain.charla import Charla
from domain.log import Log


engine = create_engine(
    'postgres://edhyrpuf:XqQEG43cSPNDDR01SdN_6jj2NqulhaGn@tuffi.db.elephantsql.com:5432/edhyrpuf',
    echo=True)

# enlaza clases con tablas
start_mappers()

# crea las tablas en la base de datos (no importa el start mapper!
metadata.create_all(engine)

# enlaza la sesion con la base de datos
Session = sessionmaker(bind=engine)

# crea una sesion
session = Session()

resultado = session.query(Parametro).first()
print(resultado)

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


# CONTROLADOR_BOT = ControladorBot()


# buena forma de agregar muchos a la vez,
# hacer una tupla
# # create catalog
tshirt, mug, hat, crowbar = (
    Charla("inactiva", "3", "4", "5", "6"),
    Charla("inactiva", "3", "4", "5", "6"),
    Charla("inactiva", "3", "4", "5", "6"),
    Charla("inactiva", "3", "4", "5", "6"),
)


# session.add(tshirt)
# session.add(mug)
# session.add(hat)
# session.add(crowbar)
session.bulk_save_objects([tshirt, mug, hat, crowbar])
with profilex.profiled():
    session.commit()
