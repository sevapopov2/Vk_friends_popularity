import vk, urllib.request, csv, json, pprint, time
from pprint import pprint
login = input("Введите имя пользователя: ")
password = input("Введите пароль: ")
session = vk.AuthSession(app_id='5889724', user_login=login, user_password=password)
api = vk.API(session)

#Количество моих записей на стене
def number_of_likes(api):
    myposts =api.wall.get()
    total_posts=myposts[0]
    i=0
    j=1
    a=0
    #print('количество моих записей на стене:')
    for i in range (0, total_posts, 100):
        myposts =api.wall.get(count=100, offset=i)
        for abc in myposts:
            #time.sleep(1) 
            try:
                a=a+int(abc['likes']['count'])
                #print(str(j) + " - " + str(a))
            except:
                print('Ошибка')
            j=j+1
        #print(a)
    return a

print(number_of_likes(api))