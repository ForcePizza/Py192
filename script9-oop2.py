# ООП продовження
class MyClass :
    x = 10                                # все, що описується у класі - статичне. Для створення об'єктних (динамічних)
                                          # використовується конструктор - метод з назвою __init__, у нього, як і у будь-який
    def __init__(self, y=20, w=30):       # інший метод прямо передається self - посилання на об'єкт (~this). Назва не
        self.y = y                        # регламентується, але традиційно "self". Звернення до об'єктних змінних -
        self.w = w                        # обов'язково через "self" (інакше - це звернення до глобальних змінних)
     
    def __str__(self) -> str:             # ~ToString()
        return f"({self.y},{self.w})"
    
    # метод, що повертає суму y+w

def main() :                              # При виклику self зв'язується автоматично, передаємо лише інші аргументи
    obj1 = MyClass()                      # (20,30)
    obj2 = MyClass( 40 )                  # (40,30)
    obj3 = MyClass( 50, 60 )              # (50,60)
    obj4 = MyClass( w = 70 )              # (20,70)
    print( obj1, obj2, obj3, obj4 )


if __name__ == "__main__" :
    main()

# Описати клас "дріб" Fraction (numerator, denominator)
# Реалізувати конструктор: з можливістю виклику як з параметрами, так і без
# Реалізувати метод виведення у формі (1/2)
# Реалізувати метод float_value для одержання числового значення дробу
# * реалізувати метод скорочення дробу ( 12/15 == 4/5 )