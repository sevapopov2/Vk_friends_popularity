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
friends =api.friends.get(count='')
#table_service.create_table('MyVkApp')

k =1
user = api.users.get(user_ids=75301884)
friends_info ={'PartitionKey': 'my_friends1', 'RowKey': str(k), 'first_name': user[0]['first_name'], 'last_name': user[0]['last_name'], 'user_id': user[0]['uid']}
batch.insert_entity(friends_info)

for f in friends:
    user = api.users.get(user_ids=f)
    k =k +1
    friends_info ={'PartitionKey': 'my_friends1', 'RowKey': str(k), 'first_name': user[0]['first_name'], 'last_name': user[0]['last_name'], 'user_id': user[0]['uid']}
    batch.insert_entity(friends_info)
    if k%10==0:
#        try:
            table_service.commit_batch('MyVkApp', batch)
            batch =TableBatch()
            print('Коммит прошёл')
#        except:
#            print('произошла ошибка.')
    print(k)
    pprint(user)
    time.sleep(1)
table_service.commit_batch('MyVkApp', batch)
