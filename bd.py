from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from adapters.orm import start_mappers, metadata

def inicializar_bd():

    engine = create_engine(
        'postgres://edhyrpuf:XqQEG43cSPNDDR01SdN_6jj2NqulhaGn@tuffi.db.elephantsql.com:5432/edhyrpuf',
        )

    # enlaza clases con tablas
    start_mappers()

    # crea las tablas en la base de datos (no importa el start mapper!
    metadata.create_all(engine)

    # enlaza la sesion con la base de datos
    Session = sessionmaker(bind=engine)

    # crea una sesion
    return Session()
