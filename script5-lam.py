# lambda - вирази

# Вираз - інструкція, що має результат (значення)
# lambda - вирази мають за результат функції (callable object)
# головна відмінність від декларованих ф-цій (def) у тому, що їх можна
# створювати під час виконання, передавати у інші ф., повертати з інших ф.
# або вживати у "одноразових" інструкціях
def lam_demo() -> None :    # перший рядок після дефініції - документація (підказка до ф-ції)
    '''Демонстрація лямбда-виразів'''
    lam1 = lambda x : print( x )
    lam1( "lam1" )
    lam2 = lambda x, y : print(x, y)
    lam2( 10, 20 )
    lam3 = lambda : print( "No args" ) 
    lam3()
    # IIFE Immediately Invoked Function Expression - Вирази миттєвого запуску
    ( lambda x : print(x) )( "IIFE" )
    true = lambda : True      # константна lambda


# модульний принцип Python, зокрема, має традицію, що програма (файл)
# може бути запущена як безпосередньно, так і у якості модуля (бібліотеки)
# Для того щоб розрізняти запуск (як програми) чи підключення (як модуля)
# у Python передбачено глобальну змінну __name__      print( __name__ )
# У разі запуску її значення - "__main__", у разі підключення - назва модуля (файла)
# Традиційно код "тіла" файлу вміщують у окрему ф-цію, наприкад, main()
# та викликають її умовно, якщо файл було саме запущено

def main() : 
    print( "Про лямбда-вирази: " )
    lam_demo()


if __name__ == "__main__" :
    main()

# x+=1  ++x  x++