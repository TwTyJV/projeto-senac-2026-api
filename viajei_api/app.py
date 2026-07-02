from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from viajei_api.database import get_session
from viajei_api.models import User
from viajei_api.schemas.message import Message
from viajei_api.schemas.user import UserList, UserPublic, UserSchemas

app = FastAPI()

database = []


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def login(user: UserSchemas, session: Session = Depends(get_session)):

    db_user = session.scalar(select(User).where((User.email == user.email)))

    if db_user:
        raise HTTPException(HTTPStatus.CONFLICT, detail="esse email já existe")

    db_user = User(email=user.email, password=user.password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.get("/users/", response_model=UserList)
def read_users(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):

    users = session.scalars(select(User).offset(skip).limit(limit)).all()
    return {"users": users}


@app.delete("/users/{user_id}", response_model=Message)
def delete_user(user_id: int, session: Session = Depends(get_session)):

    db_user = session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User not found"
        )

    session.delete(db_user)
    session.commit()

    return {"message": "User Deleted"}


@app.get("/users/{user_id}", response_model=UserPublic)
def test_delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User no foundd"
        )

    return database[user_id - 1]
