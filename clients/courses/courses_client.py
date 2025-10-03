from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient

class GetCoursesQueryDict(TypedDict):
    userId: str

class CreateCourseRequestDict(TypedDict):
    title: str
    maxScore: str
    minScore: str
    description: str
    estimatedTime: str
    previewFielId: str
    createByUserId: str


class UdpateCourseRequestDict(TypedDict):
    title: str | None
    maxScore: str | None
    minScore: str | None
    minScore: str | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    def get_courses_api(self, query) -> Response:
        return self.get(f'courses', params=query)

    def get_course_api(self, course_id: str) -> Response:
        return self.get(f'courses/{course_id}')

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        return self.post(f'courses', json=request)

    def update_course_api(self, course_id: str, request) -> Response
        return self.patch(f'courses/{course_id}', json=request)

    def delete_course_api(self, course_id: str) -> Response:
        return self.delete(f'courses/{course_id}')