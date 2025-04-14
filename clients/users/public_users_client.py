from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUsersDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """

    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def create_users_api(self, request: CreateUsersDict) -> Response:
        """
        Метод создает пользователя.

        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.post("/api/v1/users", json=request)
