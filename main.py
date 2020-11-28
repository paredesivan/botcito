from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (Table, MetaData, Column, Integer, String, SmallInteger, Boolean, Date, ForeignKey)
from sqlalchemy.orm import mapper, relationship


from sqlalchemy.ext.declarative import declarative_base



# engine = create_engine('postgres+psycopg2://mzmqoonm:xhZeUWN5TPvYKQYAQdCelh2SSx2Wpjas@suleiman.db.elephantsql.com:5432/mzmqoonm')


metadata = MetaData()

class User:
    def __init__(self, telefono_origen):
        self.telefono_origen = telefono_origen

# este es el nombre que tendra la base de datos
tabla = Table('user', metadata,
             Column('telefono_origen', String(50), primary_key=True),
             )

mapper(User, tabla)

engine = create_engine('postgres+psycopg2://mzmqoonm:xhZeUWN5TPvYKQYAQdCelh2SSx2Wpjas@suleiman.db.elephantsql.com:5432/mzmqoonm')


metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

# a = User(telefono_origen="4")

# session.add(a)

# session.commit()


# CONTROLADOR_BOT = ControladorBot()
