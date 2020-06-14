from azure.storage.table import TableService, Entity, TableBatch
table_service = TableService(account_name='seva', account_key='SgbxLwWkBH4XuGebxECoXfNVG3mVM5YjOs+SWTDUSacc+3YgUmcafYXrXdz5k0HtlZQ3AuEJ1IcFtZYeGVR9Hw==')
batch =TableBatch()

#table_service.delete_table('Tablitsa2')

#table_service.create_table('Tablitsa2')

#test2 = {'PartitionKey': 'VtorayaTablitsa', 'RowKey': '001', 'description' : 'Это вторая таблица.', 'priority' : 200}
#table_service.insert_entity('Tablitsa2', test2)
#test2 = {'PartitionKey': 'VtorayaTablitsa', 'RowKey': '002', 'description': 'Это вторая строчка таблицы.', 'priority': 200}
#table_service.insert_entity('Tablitsa2', test2)

test2 = table_service.get_entity('Tablitsa2', 'VtorayaTablitsa', '001')
print(test2.description)
print(test2.priority)
test2 = table_service.get_entity('Tablitsa2', 'VtorayaTablitsa', '002')
print(test2.description)
print(test2.priority)
#test2 = {'PartitionKey': 'VtorayaTablitsa', 'RowKey': '002', 'description': 'Это вторая обновлённая строчка таблицы.', 'priority': 100}
#table_service.update_entity('Tablitsa2', test2)
#test2 = table_service.get_entity('Tablitsa2', 'VtorayaTablitsa', '002')
#print(test2.description)
#print(test2.priority)

#test2 = {'PartitionKey': 'VtorayaTablitsa', 'RowKey': '001', 'description' : 'Проверяю замену первой строчки.', 'priority' : 200}
#table_service.insert_or_replace_entity('Tablitsa2', test2)
#test2 = table_service.get_entity('Tablitsa2', 'VtorayaTablitsa', '001')
#print(test2.description)
#print(test2.priority)

test3 = {'PartitionKey': 'VtorayaTablitsa', 'RowKey': '003', 'description': 'Проверяю функцию массовой работы с объектами.', 'priority': 300}
test4 = {'PartitionKey': 'VtorayaTablitsa', 'RowKey': '004', 'description': 'Второй пример для роверки функции массовой работы с объектами.', 'priority': 500}
batch.insert_entity(test3)
batch.insert_entity(test4)
table_service.commit_batch('Tablitsa2', batch)
tasks =table_service.query_entities('Tablitsa2', filter="PartitionKey eq 'VtorayaTablitsa'")
for test2 in tasks:
    print(test2.description)
    print(test2.priority)