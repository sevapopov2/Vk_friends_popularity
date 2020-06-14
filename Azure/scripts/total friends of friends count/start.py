import vk, urllib.request, csv, json, pprint, time
from pprint import pprint
from azure.storage.table import TableService, Entity, TableBatch

def hIndex(scores):
    if len(scores) == 0:
        return 0
    sortedScores = sorted(scores, reverse = True)
    i = 0
    for i, x in enumerate(sortedScores):
        if x < i+1:
            return i
    return len(scores)-1

def number_of_reposts(api, user_id):
    posts =api.wall.get(owner_id=user_id, count='')
    total_posts=posts[0]
    i=0
    j=1
    a=0
    retweetCountList = []
    #print('количество моих записей на стене:')
    for i in range (0, total_posts, 100):
        myposts =api.wall.get(owner_id=user_id, count=100, offset=i)
        time.sleep(1)
        for abc in myposts:
            #time.sleep(1) 
            try:
                a=a+int(abc['reposts']['count'])
                #print(str(j) + " - " + str(a))
                if a > 0 :
                    retweetCountList.append(a)
            except:
#                print('Ошибка')
                a =a
            j=j+1
        #print(a)
    return a, retweetCountList

def number_of_likes(api, user_id):
    posts =api.wall.get(owner_id=user_id, count='')
    total_posts=posts[0]
    i=0
    j=1
    a=0
    likedByOtherCountList = []
    #print('количество моих записей на стене:')
    for i in range (0, total_posts, 100):
        myposts =api.wall.get(owner_id=user_id, count=100, offset=i)
        time.sleep(1)
        for abc in myposts:
            #time.sleep(1) 
            try:
                a=a+int(abc['likes']['count'])
                #print(str(j) + " - " + str(a))
                if a > 0 :
                    likedByOtherCountList.append(a)
            except:
#                print('Ошибка')
                a =a
            j=j+1
        #print(a)
    return a, likedByOtherCountList

table_service = TableService(account_name='seva', account_key='SgbxLwWkBH4XuGebxECoXfNVG3mVM5YjOs+SWTDUSacc+3YgUmcafYXrXdz5k0HtlZQ3AuEJ1IcFtZYeGVR9Hw==')
batch =TableBatch()
#table_service.delete_table('MyVkApp')
#table_service.create_table('MyVkApp')

login = input("Введите имя пользователя: ")
password = input("Введите пароль: ")
session = vk.AuthSession(app_id='5889724', user_login=login, user_password=password)
api = vk.API(session)

#Вычисление количества друзей текущего пользователя
friends =api.friends.get(count='')

friends_list =table_service.query_entities('MyVkApp', filter="PartitionKey eq 'my_friends1'")

k =1

for friend in friends_list:
    
    try:
        friends =api.friends.get(user_id=friend.user_id, count='')
        friends_count =len(friends)
    except:
        friends_count =0
    try:
        groups =api.groups.get(user_id=friend.user_id, count='')
        groups_count =len(groups)
    except:
        groups_count =0
    try:
        posts =api.wall.get(owner_id=friend.user_id, count='')
        posts_count =posts[0]
    except:
        posts_count =0
    try:
        own_posts =api.wall.get(owner_id=friend.user_id, filter='owner')
        own_posts_count =own_posts[0]
    except:
        own_posts_count =0
    try:
        followers=api.users.getFollowers(user_id=friend.user_id)
        followers_count=int(followers['count'])
    except:
        followers_count =0

    try:
        own_posts_ratio =posts_count/own_posts_count
    except:
        own_posts_ratio =0
        
    reposts_count, reposts = number_of_reposts(api, friend.user_id)
    reposts_hIndex = hIndex(reposts)

    likes_count, scores =number_of_likes(api, friend.user_id)
    likes_hIndex = hIndex(scores)
    
    friends_info ={'PartitionKey': 'my_friends1', 'RowKey': str(k), 'first_name': friend.first_name, 'last_name': friend.last_name,
                   'user_id': friend.user_id, 'friends_count': friends_count, 'groups_count': groups_count, 'posts_count': posts_count,
                   'own_posts': own_posts_count, 'followers_count': followers_count, 'own_posts_ratio': own_posts_ratio,
                   'likes_count': likes_count, 'likes_hIndex',likes_hIndex, 'reposts_count', reposts_count, 'reposts_hIndex', reposts_hIndex}
    batch.insert_or_replace_entity(friends_info)
    if k%10==0:
        table_service.commit_batch('MyVkApp', batch)
        batch =TableBatch()
    print("#: ",k)
    print("Id: ",friend.user_id)
    print("Имя: ",friend.first_name)
    print("Фамилия: ",friend.last_name)
    print('Количество друзей: ', friends_count)
    print('Количество групп: ', groups_count)
    print('Количество постов: ', posts_count)
    print('Количество своих постов: ', own_posts_count)
    print('Количество подписчиков: ', followers_count)
    print('Соотношение своих постов со всеми постами: ', own_posts_ratio)
    print('Количество лайков: ', likes_count)
    print('hIndex likes: ',likes_hIndex)
    print('Количество репостов: ', reposts_count)
    print('hIndex репостов: ', reposts_hIndex)

    k =k +1
    time.sleep(1)
