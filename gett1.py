# Пример с параметром
import requests

# URL API с параметрами
url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': 1}  # Параметр userId

# Отправляем GET-запрос с параметрами
response = requests.get(url, params=params)

# Печатаем статус-код и содержимое ответа
print(f"Status Code: {response.status_code}")
print("Response Content:")
print(response.json())