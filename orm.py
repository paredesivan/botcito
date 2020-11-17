from sqlalchemy import (Table, MetaData, Column, Integer, String, Date, ForeignKey)
from sqlalchemy.orm import mapper, relationship
from movil import Movil


metadata = MetaData()

# si o si aca tiene que haber un primary key. sino tira error el test
tabla_movil = Table(
    'movil', metadata,
    Column('id_movil', Integer, primary_key=True, index=True),
    Column('patente', String(20))
)

tabla_servicio = Table(
    'servicio', metadata,
    Column('id_servicio', Integer, primary_key=True, index=True),
    Column('estado', String(20)),
    Column('datos', String(300)),
    Column('id_movil', ForeignKey('movil.id_movil'))
)


def start_mappers():
    # mapper(nombre de la clase, nombre objeto que devuelve Table)
    mapper(Movil, tabla_movil)
