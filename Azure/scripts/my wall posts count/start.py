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
my_posts =api.wall.get(filter='owner')
#table_service.create_table('MyVkApp')

my_posts_info ={'PartitionKey': 'my_posts', 'RowKey': '001', 'posts': my_posts[0]}
my_posts_info =table_service.insert_or_replace_entity('MyVkApp', my_posts_info)
my_posts_info =table_service.get_entity('MyVkApp', 'my_posts', '001')
print(my_posts_info.posts)