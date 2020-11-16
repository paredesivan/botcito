from movil import Movil


def test_crear_movil(session):
    session.execute(
        'INSERT INTO movil (id, patente)'
        ' VALUES ("1",  "123abc")'
    )
    expected = [Movil(1, "123abc")]
    assert session.query(Movil).all() == expected

