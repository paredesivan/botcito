from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from adapters.orm import start_mappers, metadata,add_column


engine = create_engine(
    'postgres+psycopg2://mzmqoonm:xhZeUWN5TPvYKQYAQdCelh2SSx2Wpjas@suleiman.db.elephantsql.com:5432/mzmqoonm')

# enlaza clases con tablas
start_mappers()

# crea las tablas en la base de datos
metadata.create_all(engine)

# enlaza la sesion con la base de datos
Session = sessionmaker(bind=engine)

# crea una sesion
session = Session()

# a = User(telefono_origen="4")

# session.add(a)

# session.commit()


# CONTROLADOR_BOT = ControladorBot()
