import datetime
from sqlalchemy import (Table, MetaData, Column, Integer, String, SmallInteger, Boolean, ForeignKey, DateTime)
from sqlalchemy.orm import mapper, relationship
from domain.charla import Charla
from domain.log import Log
from domain.modo import Modo
from domain.nodos.nodo import Nodo
from domain.parametro import Parametro
from domain.tag import Tag
from domain.nodos.hijos.direccion_mapa import DireccionMapa
from domain.nodos.hijos.ingresar_direccion import IngresarDireccion
from domain.nodos.hijos.seleccionar_direccion import SeleccionarDireccion
from domain.nodos.hijos.saludo import Saludo


metadata = MetaData()

tabla_charla = Table(
    'charla', metadata,
    Column('id_charla', Integer, primary_key=True, index=True, autoincrement=True),
    Column('telefono_origen', String(50), nullable=False),
    Column('estado', String(20), server_default='activa', index=True),
    Column('datos', String(200), index=True),
    Column('fecha', DateTime, index=True, default=datetime.datetime.utcnow),
    Column('telefono_destino', String(20), index=True, nullable=False),
    Column('usuario_responsable', String(50), server_default='automatico'),
    Column('intentos_fallidos', Integer, server_default='0'),
    Column('id_ultimo_nodo', ForeignKey('nodo.id'), index=True),
    Column('id_modo', ForeignKey('modo.id_modo'))
)

tabla_log = Table(
    'log', metadata,
    Column('id_log', Integer, primary_key=True, index=True, autoincrement=True),
    Column('estado', String(20), index=True, server_default='activa'),
    Column('datos', String(200), index=True),
    Column('seleccionado', Boolean, server_default='False'),
    Column('texto_ofrecido', String(200)),
    Column('fecha_hora_envio', String(50)),
    Column('opcion', String(40), index=True),
    Column('estado_envio', String(20), server_default='nuevo'),
    Column('id_charla', ForeignKey('charla.id_charla'), index=True),
    Column('id_nodo', ForeignKey('nodo.id'), index=True)
)

tabla_modo = Table(
    'modo', metadata,
    Column('id_modo', Integer, primary_key=True, index=True),
    Column('nombre', String(50))
)

tabla_nodo = Table(
    'nodo', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('id_nodo', Integer, index=True),
    Column('id_padre', ForeignKey('nodo.id'), index=True, nullable=True),
    Column('id_modo', ForeignKey('modo.id_modo'), index=True, nullable=False),
    Column('orden', SmallInteger),
    Column('nombre_subclase', String(50), nullable=False),
    Column('id_tag', ForeignKey('tag.id_tag'), index=True, nullable=True),
)

tabla_parametro = Table(
    'parametro', metadata,
    Column('id_sucursal', String(10), primary_key=True),
    Column('maximo_intentos_fallidos', Integer, server_default='3'),
    Column('automatico_encendido', Boolean, server_default='False'),
    Column('id_modo', ForeignKey('modo.id_modo'), index=True, nullable=False),
)

# # [_saludo,    buenos #hora bienvenido a #empresa,    saludo
tabla_tag = Table(
    'tag', metadata,
    Column('id_tag', String(20), primary_key=True, index=True),
    Column('texto', String(200), nullable=False),
    Column('texto_para_usuario', String(200), nullable=True),
)


def start_mappers():
    mapper(Charla, tabla_charla, properties={
        'logs': relationship(Log, backref="charla"),
        'modo': relationship(Modo, uselist=False),
        'ultimo_nodo': relationship(Nodo, uselist=False)
    })

    mapper(Log, tabla_log, properties={
        'nodo': relationship(Nodo, uselist=False)
    })

    mapper(Modo, tabla_modo)

    nodo_mapper = mapper(Nodo, tabla_nodo,
                         polymorphic_on=tabla_nodo.c.nombre_subclase,
                         polymorphic_identity='nodo',
                         properties={
                             'hijos': relationship(Nodo),
                             'modo': relationship(Modo, uselist=False),
                             'tag': relationship(Tag, uselist=False)
                         })

    mapper(Saludo, inherits=nodo_mapper, polymorphic_identity='Saludo')
    mapper(DireccionMapa, inherits=nodo_mapper, polymorphic_identity='DireccionMapa')
    mapper(SeleccionarDireccion, inherits=nodo_mapper, polymorphic_identity='SeleccionarDireccion')
    mapper(IngresarDireccion, inherits=nodo_mapper, polymorphic_identity='IngresarDireccion')

    mapper(Parametro, tabla_parametro)

    mapper(Tag, tabla_tag)


def add_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))
