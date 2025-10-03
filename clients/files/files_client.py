from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class CreateFileRequestDict(TypedDict):
    filename: str
    directory: str
    upload_file: str

class FilesClient(APIClient):
    def get_file_api(self, file_id: str) -> Response:
        return self.get(f'files/{file_id}')

    def create_file_api(self, request) -> Response:
        return self.post(
            f'files',
            data=request,
            files={"upload_file": open(request['upload_file'], 'rb')},
        )

    def delete_file_api(self, file_id: str) -> Response:
        return self.delete(f'files/{file_id}')
