import vk, urllib.request, csv, json, pprint, time
from pprint import pprint
login = input("������� ��� ������������: ")
password = input("������� ������: ")
session = vk.AuthSession(app_id='5889724', user_login=login, user_password=password)
api = vk.API(session)

#������� url � �������
url =api.users.get(fields='site')
print('url')
pprint(url)
