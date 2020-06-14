import vk, urllib.request, csv, json, pprint, time
from pprint import pprint
from azure.storage.table import TableService, Entity, TableBatch
table_service = TableService(account_name='seva', account_key='SgbxLwWkBH4XuGebxECoXfNVG3mVM5YjOs+SWTDUSacc+3YgUmcafYXrXdz5k0HtlZQ3AuEJ1IcFtZYeGVR9Hw==')
batch =TableBatch()
#table_service.delete_table('MyVkApp')
#table_service.create_table('MyVkApp')
login = input("Введите имя пользователя: ")
password = input("Введите пароль: ")
session = vk.AuthSession(app_id='5889724', user_login=login, user_password=password)
api = vk.API(session)
#Вычисление количества подписчиков текущего пользователя
url =api.users.get(fields='site')
print('количество подписчиков:')
url_info ={'PartitionKey': 'url_info', 'RowKey': '001', 'url': url}
url_info =table_service.insert_or_replace_entity('MyVkApp', url_info)
url_info =table_service.get_entity('MyVkApp', 'url_info', '001')
print(url_info.url)