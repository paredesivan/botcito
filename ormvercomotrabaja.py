class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    addresses = relationship("Address", backref="user")
    # relationship("nombre_clase_referida")

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    user_id = Column(Integer, ForeignKey('users.id'))


# ////////////////////////////////////////////////////////////////////////////////////
# One To Many. es el que mas me gusta
# A one to many relationship places a foreign key on the child table referencing the parent.
# relationship() is then specified on the parent, as referencing a collection of items represented by the child:


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    hijos = relationship("Child")


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))


# ///////////////////////////////////////////////////////////////////////
# alternativa 1 a muchos pero con backref
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child", backref="parent")


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 1 a 1. no se si es necesario el back populates
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    child = relationship("Child", uselist=False, back_populates="parent")


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="child")


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# muchos a muchos. no va en una clase, pero si en una tabla
association_table = Table('association', Base.metadata,
                          Column('left_id', Integer, ForeignKey('left.id')),
                          Column('right_id', Integer, ForeignKey('right.id'))
                          )


class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship(
        "Child",
        secondary=association_table,
        back_populates="parents")


class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
    parents = relationship(
        "Parent",
        secondary=association_table,
        back_populates="children")


# //////////////////////////////////////


# tipical clasic mapping
mapper(Parent, properties={
    'hijos': relationship(Child)
})

# ///////////////////////////////////////////////////////////////
# ejemplo de sqlalchemy

user = Table('user', metadata,
             Column('id', Integer, primary_key=True)
)
address = Table('address', metadata,
                Column('id', Integer, primary_key=True)
)
# no tendria que ser foranea?. supongo que no es obligatorio tener una foranea para
# establecer una relacion

mapper(User, user, properties={
    'addresses': relationship(Address, backref='user', order_by=address.c.id)
})

mapper(Address, address)

# mapper(claseMia,objetoTablaMia,properties={'rol':relationship(claseReferida,backref='nombre_tablamia')})

# ///////////////////////////////////////////////////////////////////

lines_mapper = mapper(model.OrderLine, order_lines)
batches_mapper = mapper(model.Batch, batches, properties={
    '_allocations': relationship(
        lines_mapper,
        secondary=allocations,
        collection_class=set,
    )
})
mapper(model.Product, products, properties={
    'batches': relationship(batches_mapper)
})

# Mapper(
# class_, local_table=None, properties=None, primary_key=None, non_primary=False, inherits=None, inherit_condition=None
# , inherit_foreign_keys=None, extension=None, order_by=False, always_refresh=False, version_id_col=None,
# version_id_generator=None, polymorphic_on=None, _polymorphic_map=None, polymorphic_identity=None, concrete=False,
# with_polymorphic=None, polymorphic_load=None, allow_partial_pks=True, batch=True, column_prefix=None,
# include_properties=None, exclude_properties=None, passive_updates=True, passive_deletes=False,
# confirm_deleted_rows=True, eager_defaults=False, legacy_is_orphan=False, _compiled_cache_size=100)
