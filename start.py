import vk, urllib.request, csv, json, pprint, time
from pprint import pprint
login = input("Введите имя пользователя: ")
password = input("Введите пароль: ")
session = vk.AuthSession(app_id='5889724', user_login=login, user_password=password)
api = vk.API(session)

#Вычисление количества подпищиков текущего пользователя
followers =api.users.getFollowers(count='')
print('подписчики')
pprint(followers)

#Вычисление количества групп текущего пользователя
groups =api.groups.get(count='')
print('Количество групп:')
pprint(len(groups))

#Вычисление количества друзей текущего пользователя
friends =api.friends.get(count='')
print('количество друзей:')
pprint(len(friends))

#with open('names.csv', 'w', newline='') as csvfile:
#    fieldnames = ['first_name', 'last_name']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel')
#    writer.writeheader()
#    for f in friends:
#        user = api.users.get(user_ids=f)
#        writer.writerow({'first_name': user[0]['first_name'], 'last_name': user[0]['last_name']})
#        pprint(user)
#        time.sleep(1)
#with open('groups.csv', 'w', newline='', encoding='utf-8') as csvfile:
#    fieldnames = ['group_name', 'group_id']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel')
#    writer.writeheader()
#    for g in groups:
#        group = api.groups.getById(group_ids=g)
#        writer.writerow({'group_name': group[0]['name'], 'group_id': group[0]['gid']})
#        pprint(group)
#        time.sleep(1)

#Количество сохранённых постов на стене
#faveposts =api.fave.getPosts()
#pprint(faveposts)

#Записи на стене
posts =api.wall.get(count='')
print('Записей на стене')
pprint(posts[0])
myposts =api.wall.get(filter='owner')
print('количество моих записей')
pprint(myposts[0])
allposts =myposts[0]/posts[0]
print('отношение равно')
pprint(allposts)

#Информация о записи на стене
postsinfo =api.wall.getById(posts='-27895931')
print('информация о записи')
pprint(postsinfo)

#упоминания
#mentions =api.newsfeed.getMentions(count='')
print('упоминаний')
#pprint(mentions)

#Наличие url в профиле
url =api.users.get(fields='site')
print('url')
pprint(url)

