# функції, виключні ситуації
def echo( x ) -> None :   # def- дефініція функції,  -> тип повернення (не обов'язково)
    print( x )            # тіло функції - за правилами оформлення блоку


# рекомендується два порожні рядки між дефініціями функцій
echo( "Hello World!" )


def exc() :
    raise TypeError("The type error")    # ~throw - створення виключення


try :
    exc()
    print( "try" )
except TypeError as err :
    print( "Type Error caught:", err )
except :
    print( "Other Error caught" )
else :
    print( "Nothing wrong" )
finally :
    print( "Finally" )

# модифікувати попередню задачу (2 відмінних числа): організувати як функцію,
# додати контроль того, що вводяться числа
def distincts() -> list :
    while True :
        x = input( "Введіть перше число " )
        try :
            x = int( x )
        except ValueError :
            print( "Це не число,", end = ' ' )
        else :
            break

    while True :          # цикл, що забезпечить відмінність х та у
        while True :      # цикл, що забезпечить числове введення
            y = input( "Введіть друге число " )
            try :
                y = int( y )
            except ValueError :
                print( "Це не число,", end = ' ' )
            else :
                break
        if x == y :
            print( "Числа однакові", end = ' ' )
        else :
            break

    return x, y


x, y = distincts()
print( x, y )
# Завдання - додати перевірку того, що числа позитивні (не приймати від'ємні числа)
# Д.З. Створити функцію, яка запитує у користувача три позитивні (додатні) числа
# усі відмінні між собою. Забезпечити контроль того, що вводяться числа (ігнорувати рядки)