from pydantic import BaseModel, ConfigDict, EmailStr


class UserSchemas(BaseModel):
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    email: EmailStr
    id: int
    model_config = ConfigDict(from_attributes=True)


class UserDB(UserSchemas):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
