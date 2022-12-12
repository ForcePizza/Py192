# MySQL database 1: Basics
import mysql.connector 

connection_info = {
    "host":     "localhost",
    "port":     3306,
    "database": "py192",
    "user":     "py192_user",
    "password": "pass_192"
}


def show_databases( connection ) :
    cursor = connection.cursor()
    sql = "SHOW DATABASES"
    cursor.execute( sql )
    print( "---------------------" )
    print( cursor.column_names )
    print ( "--------------------" )
    for row in cursor :
        print( row )


def main() :
    try :
        connection = mysql.connector.connect( **connection_info )
    except mysql.connector.Error as err :
        print( err.errno, err )
    else :
        print( "Connection OK" )
        show_databases( connection )
    


if __name__ == "__main__" :
    main()


'''
0. Встановлюємо MySQL (XAMPP), запускаємо
1. Створюємо базу даних для роботи з Python, користувача для неї
    CREATE DATABASE py192 ;
    CREATE USER py192_user@localhost IDENTIFIED BY 'pass_192' ;
    GRANT ALL PRIVILEGES ON py192.* TO py192_user@localhost ;
  Перевірка: виходимо як root, заходимо як py192_user:
    exit
    mysql -u py192_user -p
    Enter password: ******** (pass_192)
  Перевіряємо доступність БД
      SHOW DATABASES;   - у переліку має бути py192

2. Встановлюємо драйвери для узгодження ПЗ та БД (Python-MySQL)
    Рекомендація - шукати драйвери від виробника БД: у термінах MySQL/MariaDB їх
    називають коннекторами - Connector/Python
    pip3 install mariadb
    pip install mysql-connector-python
  Далі слідуємо документацією драйвера  

  Д.З. Створити функцію, яка подасть та обробить SQL-команду для виведення усіх таблиць у БД
'''