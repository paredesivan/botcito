from sqlalchemy import (Table, MetaData, Column, Integer, String, SmallInteger, Boolean, Date, ForeignKey)
from sqlalchemy.orm import mapper, relationship

from domain.charla import Charla
from domain.log import Log
from domain.modo import Modo
from domain.parametro import Parametro
from domain.servicio import Servicio
from domain.tag import Tag
from sqlalchemy.ext.declarative import declarative_base
from main import engine

metadata = MetaData()
# luego todas importan base
Base = declarative_base()
# 2 - generate database schema
Base.metadata.create_all(engine)


# usa el modo clasiccal mapping, pero despues usa los mappers para poder enlazar las clases con las tablas
# si o si aca tiene que haber un primary key por tabla. sino tira error el test
# es mas facil despues usar alembicsi uso el clasical mapping
# la forma de definir las tablas son como las de core schema pero dps hace el mapeo y queda usando el schema orm
# todas son nuleables por defecto excepto las primary key

tabla_charla = Table(
    'charla', metadata,
    Column('id_charla', Integer, primary_key=True, index=True, autoincrement=True),
    Column('telefono_origen', String(50)),
    Column('estado', String(20), server_default='activa', index=True),
    Column('telefono_destino', String(20), index=True),
    Column('usuario_responsable', String(50)),
    Column('intentos_fallidos', Integer, server_default='0'),
)
#
# tabla_log = Table(
#     'log', metadata,
#     Column('id_log', Integer, primary_key=True, index=True, autoincrement=True),
#     Column('estado', String(20), index=True, server_default='activa'),
#     Column('seleccionado', Boolean, server_default='False'),
#     Column('texto_ofrecido', String(200)),
#     Column('fecha_hora_envio', String(50)),
#     Column('opcion', String(40), index=True),
#     Column('estado_envio', String(20), server_default='nuevo'),
#     Column('id_charla', ForeignKey('charla.id_charla'))
# )
#
# tabla_modo = Table(
#     'modo', metadata,
#     Column('id_modo', SmallInteger, primary_key=True),
#     Column('nombre', String(10), unique=True),
#     Column('texto_accion', String(20)),
#     Column('funcion', String(50))
# )
#
# tabla_parametro = Table(
#     'parametro', metadata,
#     Column('id_empresa', String(10), primary_key=True),
#     Column('horarios', String(20), server_default='6,13,20'),
#     Column('maximo_intentos_fallidos', Integer, server_default='3'),
#     Column('automatico_encendido', Boolean, server_default='False'),
#     Column('modo', ForeignKey('modo.id_modo')),
# )
#
# tabla_servicio = Table(
#     'servicio', metadata,
#     Column('id_servicio', Integer, primary_key=True, index=True),
#     Column('id_movil', Integer),
#     Column('chofer', String(50)),
#     Column('patente', String(20)),
#     Column('estado', String(20)),
#     Column('datos', String(300)),
#     Column('id_charla', ForeignKey('charla.id_charla'))
# )
#
# # [_saludo,    buenos #hora bienvenido a #empresa,    saludo
# tabla_tag = Table(
#     'tag', metadata,
#     Column('id_tag', String(20), primary_key=True),
#     Column('texto', String(200), nullable=False),
#     Column('texto_para_usuario', String(30)),
#     Column('id_modo', ForeignKey('modo.id_modo'))
# )
#

def start_mappers():
    # mapper(nombre de la clase, nombre objeto que devuelve Table)
    # mapper(Charla, tabla_charla, properties={
    #     'logs': relationship(Log),
    #     'servicio': relationship(Servicio, uselist=False)
    # })
    mapper(Charla, tabla_charla)
    # mapper(Log, tabla_log)
    # mapper(Parametro, tabla_parametro)
    # # mapper(Parametro, tabla_parametro, properties={
    # #     'modo': relationship(Modo, uselist=False)
    # # })
    # mapper(Modo, tabla_modo, properties={
    #     'tags': relationship(Tag)
    # })

    # mapper(Servicio, tabla_servicio)
    # mapper(Tag, tabla_tag)
