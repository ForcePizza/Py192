import asyncio  # засоби для асинхронного програмування
import time
 
async def print_timeout(               # async - декларація утворює функцію, яка
            interval:int,              # при виклику утворює coroutine - об'єкт
            txt:str ) :                # схожий на Promise або Task, який може
    await asyncio.sleep( interval )    # виконуватись, очікуватись, відмінятись
    print( txt )                       # !! виклик async функції не запускає код
 
async def main1() :                    # запуск async функції має відбуватись 
    # print_timeout( 2, "Done" )       # за допомогою методів asyncio.run або .create_task
    task1 = asyncio.create_task(       # Недоцільно відразу чекати await print_timeout...
        print_timeout( 2, "Done1" ) )  # Користь асинхронності у тому, що поки задача виконується
    print( "Task1 created" )           #  можна робити інші команди
    task2 = asyncio.create_task(       # При правильній організації асинхронних задач спочатку
        print_timeout( 1, "Done2" ) )  # запускають найбільш тривалі задачі, після цього - менш
    print( "Task2 created" )           # тривалі, протягом їх роботи виконують швидкі задачі
    await task1                        # await намагаємость "відкласти" якомога далі, коли без
    await task2                        # результатів вже неможна працювати
    print( "Tasks finished" )          #


async def get_delayed( timeout:int, txt:str ) :
    await asyncio.sleep( timeout )
    return txt


async def main2() :
    print( "Start", time.strftime( '%X' ) )     # Неефективний підхід - разом 2+1 сек
    print( await get_delayed( 1, "Done1" ) )    #  
    print( await get_delayed( 2, "Done2" ) )    #  
    print( "Finish", time.strftime( '%X' ) )    #  

async def main3() :
    print( "Start", time.strftime( '%X' ) )                    # Більш ефективний підхід - 2 сек
    txt2 = asyncio.create_task( get_delayed( 2, "Done2" ) )    # Паралельний старт двох задач
    txt1 = asyncio.create_task( get_delayed( 1, "Done1" ) )    # 
    res = await txt1
    print( res )
    print( await txt2 )
    print( "Finish", time.strftime( '%X' ) )


# скасування задач - коли задача скасовується в її функцію передається виключення asyncio.CancelledError
# тому рекомендується тіло асинхронних функцій цілком розміщати у блоці try
async def get_or_cancel( timeout:int, txt:str ) :
    try :
        await asyncio.sleep( timeout )
        return txt
    except :
        return "Cancelled" 

async def main() :
    print( "Start", time.strftime( '%X' ) ) 
    txt2 = asyncio.create_task( get_or_cancel( 2, "Done2" ) ) 
    txt1 = asyncio.create_task( get_or_cancel( 1, "Done1" ) )
    res = await txt1
    print( res )
    if res == "Done1" :   # умовне скасування задачі
        txt2.cancel()
    print( await txt2 )
    print( "Finish", time.strftime( '%X' ) )


if __name__ == "__main__" :            #         
    # asyncio.run( main2() )           # asyncio.run просто запускає
    # asyncio.run( main3() )           # 
    asyncio.run( main() )

'''
Багатозадачність у Python
Термінологія:
 - асинхронність - одночасна робота кількох процедур
 - багатопоточність - використання системних ресурсів "потоки"
 - багатозадачність - використання мовних ресурсів "задачі"
 - синхронізація - утворення "ділянок" на яких неможливе одночасне виконання
У Python - coroutines - вживається у двох сенсах 
 а) як асинхронність 
 б) як об'єкт-задача (Future або Task)


Особливість асинхронного програмування у тому, що порядок задач "перевертається"
Д.З. Змінити порядок виклику задач у скрипті авторизації /auth:
Логіка: - перевіяємо заголовок, 
            читаємо тіло пакету, 
            виділяємо токен, 
            підключаємось до БД, 
            перевіряємо токен
Асинхр: - запускаємо підключення до БД,
            запускаємо читання тіла пакету,
            перевіяємо заголовок, (можливе скасування задач)
            чекаємо на тіло, виділяємо токен, 
            чекаємо на підключення, перевіряємо токен
'''
