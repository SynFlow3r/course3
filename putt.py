import requests

# URL, к которому будем отправлять PUT-запрос
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Новые данные для обновления заголовка поста
data = {'title': 'Updated Title'}

# Отправляем PUT-запрос с новыми данными
response = requests.put(url, json=data)

# Печатаем статус-код и содержимое ответа
print(f"Status Code: {response.status_code}")
print("Response Content:")
print(response.json())
