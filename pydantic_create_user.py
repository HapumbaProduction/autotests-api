from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(UserSchema):
    """
    Описание структуры запроса на создание пользователя.
    """
    password: str


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema
