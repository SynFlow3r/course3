import requests

# URL, к которому будем отправлять POST-запрос
url = 'https://jsonplaceholder.typicode.com/posts'

# Данные, которые будем отправлять (в данном случае, это JSON-объект)
data = {'title': 'foo', 'body': 'bar', 'userId': 1}

# Отправляем POST-запрос с данными
response = requests.post(url, json=data)

# Печатаем статус-код и содержимое ответа
print(f"Status Code: {response.status_code}")
print("Response Content:")
print(response.json())
