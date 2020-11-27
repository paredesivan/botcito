from sqlalchemy import create_engine, connectors
from sqlalchemy.orm import sessionmaker
from service_layers.controlador_bot import ControladorBot
import adapters.orm as orm


CONTROLADOR_BOT = ControladorBot()

# The PostgreSQL dialect uses psycopg2 as the default DBAPI
# igual se puede especificar que usara ese con postgresql+psycopg2 u otro postgresql+pg8000
engine = create_engine('postgres://mzmqoonm:xhZeUWN5TPvYKQYAQdCelh2SSx2Wpjas@suleiman.db.elephantsql.com:5432/mzmqoonm')
Session = sessionmaker(bind=engine)
session = Session()
orm.start_mappers()  # similar a crear schema supongo


