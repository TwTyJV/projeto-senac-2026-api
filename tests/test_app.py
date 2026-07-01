from http import HTTPStatus


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


def test_read_root(client):

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Bem vindo!"}


def test_read_user(client):

    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "email": "alice@example.com",
                "id": 1,
            }
        ]
    }


def test_delete_user(client):

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
