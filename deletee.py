import requests

# URL, к которому будем отправлять DELETE-запрос
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Отправляем DELETE-запрос
response = requests.delete(url)

# Печатаем статус-код
print(f"Status Code: {response.status_code}")
