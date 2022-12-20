#!C:/Python311/python.exe

import os
# API demo - доступ до ресурсу обмеженого доступу (Resource Server)

def send401( message:str = None ) -> None :
    print( "Status: 401 Unauthorized" )
    print( 'WWW-Authenticate: Basic realm "Authorization required" ')
    print()
    if message :
        print( message )
    return
    
    
# дістаємо заголовок Authorization
if 'HTTP_AUTHORIZATION' in os.environ.keys() :
    auth_header = os.environ['HTTP_AUTHORIZATION']
else :
    # відправляємо 401
    send401()
    exit()

if auth_header.startswith( 'Basic' ) :
    credentials = auth_header[6:]
else :
    send401( "Authorization scheme Basic required" )
    exit()

# credentials (параметр заголовку) - це Base64 кодований рядок "логін:пароль"
# у скрипті info підготуємо зразок для "admin:123"  --> 



# '''
# Схеми авторизації.
# https://datatracker.ietf.org/doc/html/rfc6750

# Запит на обмежений ресурс --> Перевірка авторизації
# якщо "+", то видаємо ресурс, інакше відповідь з кодом 401

# Перевірка авторизації: аналіз заголовку Authorization
# та відповідної схеми автентифікації
#  - Basic - безпосередня передача логіну та паролю (кодованих у Base64)
#  - Bearer - за допомогою спеціальних токенів

# Токен отримується від серверу авторизації /auth
# '''