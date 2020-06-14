import vk, urllib.request, csv, json, pprint, time
from pprint import pprint
login = input("Введите имя пользователя: ")
password = input("Введите пароль: ")
session = vk.AuthSession(app_id='5889724', user_login=login, user_password=password)
api = vk.API(session)

#Наличие url в профиле
url =api.users.get(fields='site')
print('url')
pprint(url)
