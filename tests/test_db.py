from dataclasses import asdict

from sqlalchemy import select

from viajei_api.models import Story, User


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

    assert asdict(user) == {
        "id": 1,
        "password": "senha123",
        "email": "joao@test.test",
        "created_at": time,
    }


def test_creat_story(session, mock_db_time, user):
    with mock_db_time(model=Story) as time:
        new_story = Story(author="jj", title="Titulo", story="Era uma vez...")

        new_story.email = user.email

        session.add(new_story)
        session.commit()

    story = session.scalar(select(Story).where(Story.author == "jj"))

    assert asdict(story) == {
        "id": 1,
        "author": "jj",
        "title": "Titulo",
        "email": "exempl@exemple.com",
        "story": "era uma vez...",
        "created_at": time,
    }
