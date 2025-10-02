from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class LoginRequest(TypedDict):
    email: str
    password: str

class RefreshRequestDict(TypedDict):
    refreshToken: str

class AuthenticationClient(APIClient):
    def login_api(self, request: dict) -> Response:
        return self.post("/api/v1/authentication/login", json=request)


    def refresh_api(self, request: RefreshRequestDict) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request)