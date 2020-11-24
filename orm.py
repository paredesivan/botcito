from sqlalchemy import (Table, MetaData, Column, Integer, String, Date, ForeignKey)
from sqlalchemy.orm import mapper, relationship
from movil import Movil
from servicio import Servicio
from charla import Charla


metadata = MetaData()

# si o si aca tiene que haber un primary key. sino tira error el test
tabla_movil = Table(
    'movil', metadata,
    Column('id_movil', Integer, primary_key=True, index=True),
    Column('patente', String(20))
)

# como el schema core, pero dps hace el mapeo y queda usando el schema orm
tabla_servicio = Table(
    'servicio', metadata,
    Column('id_servicio', Integer, primary_key=True, index=True),
    Column('estado', String(20)),
    Column('datos', String(300)),
    Column('id_movil', ForeignKey('movil.id_movil'))
)

tabla_charla = Table(
    'charla', metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('telefono_origen', String(50)),
    Column('estado', String(20)),
    Column('telefono_destino', String(50)),
    Column('usuario_responsable', String(50)),
    Column('intentos_fallidos', Integer),

)


def start_mappers():
    # mapper(nombre de la clase, nombre objeto que devuelve Table)
    mapper(Movil, tabla_movil)
    mapper(Servicio, tabla_servicio)
    mapper(Charla, tabla_charla)
