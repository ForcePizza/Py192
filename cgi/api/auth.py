#!C:/Python311/python.exe

import os, base64
# Authorization Server

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

# Перевіряємо схему авторизації - має бути Basic
if auth_header.startswith( 'Basic' ) :
    credentials = auth_header[6:]
else :
    send401( "Authorization scheme Basic required" )
    exit()

# credentials (параметр заголовку) - це Base64 кодований рядок "логін:пароль"
# у скрипті info підготуємо зразок для "admin:123"  --> YWRtaW46MTIz
# декодуємо credentials
try :
    data = base64.b64decode( credentials, validate=True ).decode( 'utf-8' )
except :
    send401( "Credentials invalid: Base64 string required" )
    exit()

# Перевіряємо формат (у data має бути :)
if not ':' in data :
    send401( "Credentials invalid: Login:Password format expected" )
    exit()

user_login, user_password = data.split( ':', maxsplit = 1 )

# Успішне завершення
print( "Status: 200 OKey" )
print( "Content-Type: text/plain" )
print()
print( user_login, user_password )
