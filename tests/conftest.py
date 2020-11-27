import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from adapters.orm import metadata, start_mappers


@pytest.fixture
def in_memory_db():
    engine = create_engine('postgres://mzmqoonm:xhZeUWN5TPvYKQYAQdCelh2SSx2Wpjas@suleiman.db.elephantsql.com:5432/mzmqoonm')
    # engine = create_engine('sqlite:///:memory:')
    metadata.create_all(engine)
    return engine


@pytest.fixture
def session(in_memory_db):
    start_mappers()
    yield sessionmaker(bind=in_memory_db)()
    clear_mappers()