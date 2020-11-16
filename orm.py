from sqlalchemy import (Table, MetaData, Column, Integer, String, Date, ForeignKey)
from sqlalchemy.orm import mapper, relationship
from movil import Movil


metadata = MetaData()

# si o si aca tiene que haber un primary key. sino tira error el test
tabla_movil = Table(
    'movil', metadata,
    Column('id', Integer, primary_key=True),
    Column('patente', String(20))
)


def start_mappers():
    # mapper(nombre de la clase, nombre objeto que devuelve Table)
    mapper(Movil, tabla_movil)
