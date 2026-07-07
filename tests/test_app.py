from http import HTTPStatus

from viajei_api.schemas.user import UserPublic


def test_create_user(client):

    response = client.post(
        "/users/",
        json={
            "email": "alice@example.com",
            "password": "secret",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "email": "alice@example.com",
        "id": 1,
    }


def test_read_user(client):

    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"users": []}


def test_read_user_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get("/users/")

    assert response.json() == {"users": [user_schema]}


def test_delete_user(client, user):

    response = client.delete("/users/1")

    response.status_code == HTTPStatus.OK
    response.json() == {"message": "User deletad!"}


def test_deleti_user(client):

    response = client.delete("/users/3")

    response.status_code == HTTPStatus.NOT_FOUND
    response.json() == {"detail": "user not foundd"}


def ex_cliente(client):

    response = client.get("/users/5")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"detail": "user not found"}


def ex_user(client):

    response = client.delete("/users/3")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "joao",
        "email": "jao@ex.exxx",
        "id": 1,
    }


def test_get_token(client, user):
    response = client.post(
        "/auth",
        data={
            "username": user.email,
            "password": user.clean_password,
        },
    )

    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert "access_token" in token
    assert "token_type" in token


def test_create_story(authenticated_user):

    response = authenticated_user.post(
        "/story",
        json={
            "author": "joao",
            "title": "copa",
            "story": "Era uma vez",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "title": "copa",
        "email": "exempl@exempl.com",
    }
