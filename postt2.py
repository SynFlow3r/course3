# Пример для создания нового пользователя с его постом 
import requests

# URL API для создания нового пользователя
url_users = 'https://jsonplaceholder.typicode.com/users'
url_posts = 'https://jsonplaceholder.typicode.com/posts'

# Данные, которые будем отправлять для создания нового пользователя
user_data = {
    'name': 'John Doe',
    'username': 'johndoe',
    'email': 'john.doe@example.com',
}

# Отправляем POST-запрос для создания нового пользователя
user_response = requests.post(url_users, json=user_data)
user_id = user_response.json().get('id')

# Данные, которые будем отправлять для создания нового поста от пользователя
post_data = {
    'userId': user_id,
    'title': 'New Post',
    'body': 'This is a new post created by John Doe.',
}

# Отправляем POST-запрос для создания нового поста
post_response = requests.post(url_posts, json=post_data)

# Печатаем статус-код и содержимое ответа для обоих запросов
print(f"User Creation Status Code: {user_response.status_code}")
print("User Creation Response Content:")
print(user_response.json())

print(f"\nPost Creation Status Code: {post_response.status_code}")
print("Post Creation Response Content:")
print(post_response.json())
