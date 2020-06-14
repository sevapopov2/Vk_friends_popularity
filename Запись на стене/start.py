import vk

vkapi = vk.API(v='5.60', app_id ='5889724', user_login = 'sevapopov13@gmail.com', user_password ='uchebnik1', access_token = '96a932773fa521c67719a86ba30d49f90245e946e241a583c82b57cd2970f58aef41ea5f7c1bfd4d61077')

vkapi.wall.post(message="Hello, world")