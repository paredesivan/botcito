from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from adapters.orm import start_mappers, metadata
from domain.parametro import Parametro
from domain.charla import Charla
from domain.log import Log

engine = create_engine(
    'postgres://edhyrpuf:XqQEG43cSPNDDR01SdN_6jj2NqulhaGn@tuffi.db.elephantsql.com:5432/edhyrpuf')

# enlaza clases con tablas
start_mappers()

# crea las tablas en la base de datos (no importa el start mapper!
metadata.create_all(engine)

# enlaza la sesion con la base de datos
Session = sessionmaker(bind=engine)

# crea una sesion
session = Session()


# resultado=session.query(Parametro).first()

# print("modo_del_parametro:",resultado)
# a=Charla("activo",3,"teldefino,","teorigen","respo44")
# a=Log(1,"activa",False,"hola perri2","hoy","2","nuevo")
# session.add(a)
# session.commit()

log=Log(1,"43",False,"hola","123","1","nuevo")
charla=Charla("1","3","4","5","6")
charla.clogs.add(log)
print(charla.clogs)
    # print("camello:",r.camello)
    # print("logs")

# for x in session.query(Log):
#     print(x)
#     print(x.id_charla)
#     print(x.charla)



# session.add(charla)
# session.commit()



# CONTROLADOR_BOT = ControladorBot()
