from fastapi import FastAPI

from pydantic import BaseModel, Field, EmailStr, ConfigDict

app = FastAPI()

data = {
    "email": "test@test.ru",
    "bio": "Босс",
    "age": 18,
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str = Field(max_length=1000)

    model_config = ConfigDict(extra="forbid")


users = []


@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {"msg": "Юзер добавлен"}


@app.get("/users")
def get_users() -> list[UserSchema]:
    return users


class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=100)


# user = UserAgeSchema(**data)
# print(repr(user))
