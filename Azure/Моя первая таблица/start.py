from azure.storage.table import TableService, Entity
table_service = TableService(account_name='seva', account_key='SgbxLwWkBH4XuGebxECoXfNVG3mVM5YjOs+SWTDUSacc+3YgUmcafYXrXdz5k0HtlZQ3AuEJ1IcFtZYeGVR9Hw==')

#table_service.delete_table('tasktable')

#table_service.create_table('Table1')

#test1 = {'PartitionKey': 'tasksSeattle', 'RowKey': '001', 'description' : 'This is the first table for testing', 'priority' : 200}
#table_service.insert_entity('Table1', test1)

test1 = table_service.get_entity('Table1', 'tasksSeattle', '001')
print(test1.description)
print(test1.priority)
