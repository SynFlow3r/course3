import requests

# Укажите URL, к которому вы хотите выполнить GET-запрос
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Отправляем GET-запрос
response = requests.get(url)

# Печатаем статус-код и содержимое ответа
print(f"Status Code: {response.status_code}")
print("Response Content:")
print(response.json())
