# Python - REPL cистема (Read-Eval-Print-Loop) - мова-інтерпретатор
# широткого вжитку, але орієнтована на наукову галузь
# За парадигмою - близька до функціональної (хоча є змішаною)
# Змінні існують, типізація динамічна, але при записі
x = 10         # х набуває значення 10 (int) і зберігає тип
               # але між цими командами х - це int(10)
x = "123"      # х змінює як значення, так і тип

# print( x + 1 )     # TypeError: can only concatenate str (not "int") to str
print( x + str(1) )  # 1231
print( int(x) + 1 )  # 124

print( type(10) )        # <class 'int'>
print( type(10.5) )      # <class 'float'>
print( type(10 + 3j) )   # <class 'complex'>
print( type( x ) )       # <class 'str'>
print( type( True ) )    # <class 'bool'>
print( type( None ) )    # <class 'NoneType'>
print( x.capitalize() )
