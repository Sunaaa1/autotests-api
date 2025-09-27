import httpx

response = httpx.get('http://jsonplaceholder.typicode.com/todos/1')

print(response.status_code)
print(response.json())


data = {
    "title": "Новая задача",
    "Completed": False,
    "UserId": 1
}
response = httpx.post('http://jsonplaceholder.typicode.com/todos', json=data)

print(response.status_code)
print(response.json())


data = {"Username": "test_user", "password": "12345"}
response = httpx.post('https://httpbin.org/post', data=data)

print(response.status_code)
print(response.json())