from dataclasses import asdict

from sqlalchemy import select

from viajei_api.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(email="joao@test.test", password="senha123")

        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.email == "joao@test.test"))

    assert asdict(user) == {
        "id": 1,
        "password": "senha123",
        "email": "joao@test.test",
        "created_at": time,
    }
