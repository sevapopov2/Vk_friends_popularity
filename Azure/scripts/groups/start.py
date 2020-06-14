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
groups =api.groups.get(count='')
#table_service.create_table('MyVkApp')

k =0
for g in groups:
    group = api.groups.getById(group_ids=g)
    k =k +1
#        writer.writerow({'group_name': group[0]['name'], 'group_id': group[0]['gid']})
    groups_info ={'PartitionKey': 'my_groups', 'RowKey': str(k), 'group_name': group[0]['name'], 'group_id': group[0]['gid']}
    batch.insert_entity(groups_info)
    if k%10==0:
#        try:
            table_service.commit_batch('MyVkApp', batch)
            batch =TableBatch()
            print('Коммит прошёл')
#        except:
#            print('произошла ошибка.')
    print(k)
    pprint(group)
    time.sleep(1)
table_service.commit_batch('MyVkApp', batch)
