

def add(a,b):
    return a+b



def subtract(a,b):
    return a-b



def multiply(a,b):
    return a*b



def divide(a,b):

    if b == 0:
        return "Ошибка"

    return a/b



def main():

    print("Calculator")


    a=float(
        input("Первое число: ")
    )


    operation=input(
        "Операция (+,-,*,/): "
    )


    b=float(
        input("Второе число: ")
    )



    if operation=="+":
        print(add(a,b))


    elif operation=="-":
        print(subtract(a,b))


    elif operation=="*":
        print(multiply(a,b))


    elif operation=="/":
        print(divide(a,b))


if __name__=="__main__":
    main()

