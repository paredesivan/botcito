from sqlalchemy import (Table, MetaData, Column, Integer, String, Boolean, Date, ForeignKey)
from sqlalchemy.orm import mapper, relationship

from charla import Charla
from log import Log
from modo import Modo
from movil import Movil
from parametro import Parametro
from servicio import Servicio
from tag import Tag


metadata = MetaData()

# si o si aca tiene que haber un primary key. sino tira error el test
tabla_movil = Table(
    'movil', metadata,
    Column('id_movil', Integer, primary_key=True, index=True),
    Column('patente', String(20)),
    Column('chofer',String(30))
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
    Column('estado', String(20), server_default='activa'),
    Column('telefono_destino', String(50)),
    Column('usuario_responsable', String(50)),
    Column('intentos_fallidos', Integer, server_default=0),
)

tabla_modo = Table(
    'modo', metadata,
    Column('id', String(5), primary_key=True),
    Column('nombre', String(10), unique=True),
    Column('texto_accion', String(20)),
    Column('funcion', String(50))
)

tabla_log = Table(
    'log', metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('estado', String(20), index=True, server_default='activa'),
    Column('seleccionado', Boolean, server_default=False),
    Column('texto_ofrecido', String(200)),
    Column('fecha_hora_envio', String(50)),
    Column('opcion', String(10), index=True),
    Column('estado_envio', String(20), server_default='nuevo')
)

tabla_parametro = Table(
    'parametro', metadata,
    Column('id_empresa', String(10), primary_key=True),
    Column('horarios', String(20)),
    Column('maximo_intentos_fallidos', Integer, server_default=3),
    Column('automatico_encendido', Boolean, server_default=False)
)

tabla_tag = Table(
    'tag', metadata,
    Column('id', String(20), primary_key=True),
    Column('texto', String(30)),
    Column('texto_para_usuario', String(30))
)


def start_mappers():
    # mapper(nombre de la clase, nombre objeto que devuelve Table)
    mapper(Charla, tabla_charla)
    mapper(Log, tabla_log)
    mapper(Modo, tabla_modo)
    mapper(Movil, tabla_movil)
    mapper(Parametro, tabla_parametro)
    mapper(Servicio, tabla_servicio)
    mapper(Tag, tabla_tag)
