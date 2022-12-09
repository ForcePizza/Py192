# робота з файлами, частина 1
def write_file_1() -> None :
    try :
        with open( "file1.txt", "w", encoding = "utf-8" ) as f :   # ~ using/try()
            f.write( "Line 1\n" )
            f.write( "Line 2\n" )
            f.write( "Line 3" )
    except OSError as err :
        print( err.strerror )


def write_file1() -> None :   # прямий доступ до ресурсу
    try :
        f = open( "file1.txt", "w", encoding = "utf-8" )
    except OSError as err :
        print( err.strerror )
    else :
        f.write( "Line 1\n" )
        f.write( "Line 2\n" )
        f.write( "Line 3" )
        f.flush()
        f.close()


def read_file1() -> str | None :
    try :
        f = open( "file1.txt", mode = "r", encoding = "utf-8" )
    except FileNotFoundError as err :
        print( err.strerror )
    else :
        return f.read()
    finally :
        # print( "Finally works" )
        if f == None :
            return None
        f.close()


def read_file_1() -> str | None :
    try :
        with open( "file1.txt" ) as f :
            return f.read()
    except FileNotFoundError as err :
        print( err.strerror )
        return None


def read_lines() -> None :
    try :
        with open( "file1.txt" ) as f :
            # n = 1
            # for line in f.readlines() :   # \n залишається у рядку line
            #     print( n, line,  end = '' )
            #     n += 1
            for n, line in enumerate( f.readlines() ) :
                print( n + 1, line,  end = '' )
    except FileNotFoundError as err :
        print( err.strerror )
        return None


def main() -> None :
    # print( read_file_1() )
    read_lines()


def main1() :  # приклад ф-ції з порожнім тілом
    pass       # NOP (NoOperation) {} - "заглушка" для порожнього блоку


if __name__ == "__main__" :
    # write_file1(); exit(0)
    main()
