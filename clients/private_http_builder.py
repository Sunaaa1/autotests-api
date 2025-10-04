from typing import TypedDict

from httpx import Client

from clients.authentication.authentication_client import LoginRequestDict, get_authentication_client


class AuthenticationUserDict(TypedDict):
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserDict) -> Client:
    authentication_client = get_authentication_client()

    login_request = LoginRequestDict(email=user["email"], password=user["password"])
    login_response = authentication_client.login(login_request)
    token = login_response['token']['accessToken']

    return Client(
        timeout=100,
        base_url='http://localhost:8000',
        headers={"Authorization": f'Bearer {token}'},
    )