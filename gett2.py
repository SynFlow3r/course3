# Пример с выводом загаловки и тело первого поста
import requests

# URL API
url = 'https://jsonplaceholder.typicode.com/posts'

# Отправляем GET-запрос
response = requests.get(url)

# Печатаем только заголовки из ответа
print("Response Headers:")
print(response.headers)

# Получаем JSON-список из ответа
posts = response.json()

# Выводим только заголовки и тело первого поста
if posts:
    first_post = posts[0]
    print("\nFirst Post Title:")
    print(first_post.get('title'))
