from sqlalchemy import (Table, MetaData, Column, Integer, String, SmallInteger, Boolean, Date, ForeignKey)
from sqlalchemy.orm import mapper, relationship
from domain.charla import Charla
from domain.log import Log
from domain.mensaje import Mensaje
from domain.modo import Modo
from domain.parametro import Parametro
from domain.servicio import Servicio


metadata = MetaData()

# usa el modo clasiccal mapping, pero despues usa los mappers para poder enlazar las clases con las tablas
# si o si aca tiene que haber un primary key por tabla. sino tira error el test
# es mas facil despues usar alembicsi uso el clasical mapping
# la forma de definir las tablas son como las de core schema pero dps hace el mapeo y queda usando el schema orm
# todas las columnas son nuleables por defecto excepto las primary key
# las primary key NO son indices por defecto
# los autoincrements de las tablas no necesitan estar en la clase. es mas, no se como se pondrian
# las clases pueden tener sus propios campos sin estar enlazados a columnas en tablas.
#    tener cuidado que si no esta en la tabla, no lo recuperara al hacer la consulta a la bd
#   lo que este en la relationship si se podra obtener. de alguna manera lo guarda en la bd.
# habria que ver si tambien es recomensable poner la instancia en la clase
# todo_ lo que ponga en las tablas aparecera en la tabla (sin importar si en la clase hay mas atributos)

# las claves foraneas deberian ser indices para mejorar rendimiento en los joins
# fk evita redundancia datos
# fk garantiza integridad
# la clave foranea declarada en la tabla tambien DEBE ser un atributo en la clase

# el relationship parece que se puede poner en el lado del 1 o del muchos.
# es una relacion. no es una columna de la tabla!
#   sirve para acceder al/a los objeto/s relacionado/s.
#   es mas lento en teoria (no mucho), pero mejor y mas facil
# NO SE DEBE declarar una columna en la tabla con el nombre de la relationship
# si a la relacion le pongo backref="tablaActual" significa que TAMBIEN desde la otra tabla
#   podre acceder a mi objeto mediante el atributo "tablaActual"
# interpreto que siempre es recomensable usar backref, asi es mas facil si lo necesito

# supongo que cuando hace el add o el commit, busca los atributos en las tablas y los compara con los que tiene actualmente
#   la clase e inserta los que coinciden nomas, si falta alguno en la clase tira error porque insertaria un null


tabla_charla = Table(
    'charla', metadata,
    Column('id_charla', Integer, primary_key=True, index=True, autoincrement=True),
    Column('telefono_origen', String(50), nullable=False),
    Column('estado', String(20), server_default='activa', index=True),
    Column('telefono_destino', String(20), index=True, nullable=False),
    Column('usuario_responsable', String(50)),
    Column('intentos_fallidos', Integer, server_default='0'),

)

tabla_log = Table(
    'log', metadata,
    Column('id_log', Integer, primary_key=True, index=True, autoincrement=True),
    Column('estado', String(20), index=True, server_default='activa'),
    Column('seleccionado', Boolean, server_default='False'),
    Column('texto_ofrecido', String(200)),
    Column('fecha_hora_envio', String(50)),
    Column('opcion', String(40), index=True),
    Column('estado_envio', String(20), server_default='nuevo'),
    Column('id_charla', ForeignKey('charla.id_charla'), index=True)
)

tabla_modo = Table(
    'modo', metadata,
    Column('id_modo', SmallInteger, primary_key=True, index=True),
    Column('nombre', String(50), unique=True),

)

tabla_parametro = Table(
    'parametro', metadata,
    Column('id_empresa', String(10), primary_key=True),
    Column('horarios', String(20), server_default='6,13,20'),
    Column('maximo_intentos_fallidos', Integer, server_default='3'),
    Column('automatico_encendido', Boolean, server_default='False'),
    Column('id_modo', ForeignKey('modo.id_modo'), index=True, nullable=False),
)

tabla_servicio = Table(
    'servicio', metadata,
    Column('id_servicio', Integer, primary_key=True, index=True),
    Column('id_movil', Integer),
    Column('chofer', String(50)),
    Column('patente', String(20)),
    Column('estado', String(20)),
    Column('datos', String(300)),
    Column('id_charla', ForeignKey('charla.id_charla'), index=True)
)

# # [_saludo,    buenos #hora bienvenido a #empresa,    saludo
tabla_mensaje = Table(
    'mensaje', metadata,
    Column('id_mensaje', String(20), primary_key=True, index=True),
    Column('texto', String(200), nullable=False),
    Column('texto_para_usuario', String(30)),
    Column('id_modo', ForeignKey('modo.id_modo'), index=True)
)


def start_mappers():
    # mapper(nombre de la clase, nombre del objeto de tipo Table creado)


    mapper(Charla, tabla_charla, properties={
        'logs': relationship(Log, backref="charla"),
        'servicio': relationship(Servicio, uselist=False)
    })
    # donde dice backref quiere decir que
    # si hago charla.logs mostrara todas las instancias de logs que corresponden a la charla
    # y si en log hago log.charla mostrara el objeto entero de tipo charla que referencia a ese log

    mapper(Log, tabla_log)

    mapper(Modo, tabla_modo)

    # lo que va en relationship NO CREA UN CAMPO EN LA TABLA
    # permite recuperar las instancias asociadas
    # similar a
    # class parametro
    #     self.modo=modo() #relacion 1 a 1
    # class parametro
    #     self.direcciones=set() #set de direcciones relacion 1 a m

    # no es obligatorio tener una foranea para establecer una relacion
    # es necesario que la relacion tambien sea un atributo en la clase, no obligatorio pero si recomendable???????????
    #   porque en el libro pone la relacion dentro de la clase porque sigue el esquema orm puro

    # lazy=False hace un left outer join
    # por defecto es lazy True
    mapper(Parametro, tabla_parametro, properties={
        'modo_del_parametro': relationship(Modo, uselist=False)  # relacion 1 a 1, declara
        # un atributo modo_del_parametro dentro de la clase parametro que me permite acceder
        # al objeto referenciado
    })

    mapper(Servicio, tabla_servicio)

    # mapper(Mensaje, tabla_mensaje)


def add_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))
