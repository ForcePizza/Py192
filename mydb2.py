# Робота з БД. Продовження
import mysql.connector
import random

def select_test( db : mysql.connector.MySQLConnection, order='U' ) -> None :
    ''' Prints table 'test' data depending on 'order' parameter: 'U'(default)-Unicode, 'G'-General '''
    sql = "SELECT * FROM test t ORDER BY " + ( 't.str' if order == 'G' else 't.ukr' )
    try :
        cursor = db.cursor()    
        cursor.execute( sql )  
    except mysql.connector.Error as err :
        print( 'SELECT:', err )
    else :
        row = cursor.fetchone(); print( row )
        row = cursor.fetchone(); print( row )
        row = cursor.fetchone(); print( row )
        row = cursor.fetchone(); print( row )
        row = cursor.fetchone(); print( row )
        row = cursor.fetchone(); print( row )
        row = cursor.fetchone(); print( row )
        row = cursor.fetchone(); print( row )
    finally :
        try: 
            db.commit()     # InternalError("Unread result found") - якщо не всі дані "забрано"
            cursor.close()
        except: pass
    return


def rand_str() -> str :
    alf = "АБВГҐДЕЄЖЗИІЇКЛМНОПРСТУФХЦЧШЩЬЮЯ"
    return ''.join( random.choice(alf) for i in range( random.choice([3,4,5]) ) )


def insert_test( db : mysql.connector.MySQLConnection ) -> None :
    ''' Inserts random values into 'test' table '''
    sql = "INSERT INTO test( num, str, ukr ) VALUES ( %s, %s, %s )"
    str = rand_str()
    num = random.randint(1, 20)
    try :
        cursor = db.cursor()                     # відкриття курсора - створює транзакцію
        cursor.execute( sql, (num, str, str) )   # виконання команди - планується
    except mysql.connector.Error as err :
        print( 'INSERT:', err )
    else :
        print( 'INSERT: OK' )
    finally :
        db.commit()
        cursor.close()                           # закриття курсора без коміту транзакції - відміняє її
    return     
   

def create_table( db : mysql.connector.MySQLConnection ) -> None :
    ''' Creates table 'test' in DB '''
    sql = ''' 
    CREATE TABLE   IF NOT EXISTS   test ( 
        `id`     CHAR(36)     PRIMARY KEY    DEFAULT UUID(),
        `num`    INT          DEFAULT 0,
        `str`    VARCHAR(9)   COLLATE utf8_general_ci,
        `ukr`    VARCHAR(9)   COLLATE utf8_unicode_ci
    ) ENGINE = InnoDB, DEFAULT CHARSET = UTF8
    '''
    try :
        cursor = db.cursor()
        cursor.execute( sql )
    except mysql.connector.Error as err :
        print( 'CREATE:', err )
    else :
        print( 'CREATE: OK' )
    finally :
        cursor.close()
    return 


def main( db_conf ) -> None :
    try :
        connection = mysql.connector.connect( **db_conf )
    except mysql.connector.Error as err :
        print( err.errno, err )
    else :
        print( "Connection OK" )
        # create_table( connection )
        # insert_test( connection )
        select_test( connection )
    return


if __name__ == "__main__" :
    db_conf = {
        "host":     "localhost",
        "port":     3306,
        "database": "py192",
        "user":     "py192_user",
        "password": "pass_192",

        "use_unicode": True,
        "charset":     "utf8mb4",
        "collation":   "utf8mb4_general_ci"
    }
    main( db_conf )
