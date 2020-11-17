from movil import Movil


def test_crear_movil(session):
    session.execute(
        'INSERT INTO movil (id_movil, patente)'
        ' VALUES ("1",  "123abc")'
    )
    expected = [Movil(1, "123abc")]
    assert session.query(Movil).all() == expected


def test_crear_loco(session):
    movil = Movil(2, "4343av")
    session.add(movil)
    session.commit()
    assert session.query(Movil).all() == [movil]
