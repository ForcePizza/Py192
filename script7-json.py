# робота з JSON
import json   # підключення модуля, далі його ф-ції доступні за іменем json

def main() -> None :
    j = json.load( open( "file2.json" ) ) 
    print( type(j), j )       # <class 'dict'> {'x': 10, ... - асоціативний масив
    print( j["x"] )           # доступ до елементів - через ['key']
    for k in j :              # ітерування словника - іде по ключах
        print( "j['%s'] = %s" % ( k, j[k] ) )

    print( "-------------------" )
    for v in j.values() :     # ітерування по значеннях
        print( type(v), v )   # перебігається лише перший рівень (без заглиблення)

    print( "-------------------" )
    for k,v in j.items() :    # ітерування по парах ключ-значення
        print( k, v ) 

    j["new"] = "Вітання"      # додаємо значення у Unicode ( "new": "\u0412\u0456\u0442\u0430\u043d\u043d\u044f" - Escaping)
    print( json.dumps(              # decode / stringify / serialize
        j,                          # об'єкт для серіалізації
        indent = 4,                 # pretty-print (з розривом рядків та відступом 4 пробіли)
        ensure_ascii = False ) )    # не перетворювати на ASCII (без escaping)


if __name__ == "__main__" :
    main()

'''
Реалізувати наступну задачу:
користувач вводить дані за схемою
 key=value
Введення множинне, Кінець введення - порожній рядок
програма зберігає усі введені дані у форматі JSON у файлі 
'''