import math

z = input("Do you want 2 or 3 values? ")
if z == "Is Woo43 the dev?":
    print("Yes.")
elif z == "two" or z == "2":
    # code for the values
    print("Value 1:")
    a = int(input())
    print("Value 2:")
    b = int(input())
    print(
        "Choose your operator: + and plus, -  and minus, * and multiply,  / and divide, = and equals, sqrt 1, sqrt 2, cube a, cube b square a, or square b."
    )
    # calculation code
    op = input()
    if op == "+" or op == "plus":
        print(a + b)
    elif op == "-" or op == "minus":
        print(a - b)
    elif op == "*" or op == "multiply":
        print(a * b)
    elif op == "/" or op == "divide":
        if b == 0:
            print("Nice try.")
        else:
            print(a / b)
    elif op == "=" or op == "equals":
        if a == b:
            print("True.")
        elif a > b:
            print("False, a > b.")
        else:
            print("False, a < b.")
    elif op == "square a":
        print(a * a)
    elif op == "square b":
        print(b * b)
    elif op == "cube a":
        print(a * a * a)
    elif op == "cube b":
        print(b * b * b)
    elif op == "sqrt 1":
        print(math.sqrt(a))
    elif op == "sqrt 2":
        print(math.sqrt(b))
    # else code/error
    else:
        print("Looks like you made a typo. Sorry about that.")
elif z == "three" or z == "3":
    # code for the values
    print("Value 1:")
    a = int(input())
    print("Value 2:")
    b = int(input())
    print("Value 3:")
    c = int(input())
    print(
        "Choose your operator: + or plus, -  or minus, * or multiply,  / or divide, sqrt 1, sqrt 2, sqrt 3, square a, square b, square c, cube a, cube b, or cube c."
    )
    # calculation code
    op = input()
    if op == "+" or op == "plus":
        print(a + b + c)
    elif op == "-" or op == "minus":
        print(a - b - c)
    elif op == "*" or op == "multiply":
        print(a * b * c)
    elif op == "/" or op == "divide":
        if b == 0 or c == 0:
            print("Nice try.")
        else:
            print(a / b / c)
    elif op == "cube a":
        print(a * a * a)
    elif op == "cube b":
        print(b * b * b)
    elif op == "cube c":
        print(c * c * c)
    elif op == "square a":
        print(a * a)
    elif op == "square b":
        print(b * b)
    elif op == "square c":
        print(c * c)
    elif op == "sqrt 1":
        print(math.sqrt(a))
    elif op == "sqrt 2":
        print(math.sqrt(b))
    elif op == "sqrt 3":
        print(math.sqrt(c))
    # error
    else:
        print("Looks like you made a typo. Sorry about that.")
else:
    print("Looks like you made a typo. Sorry about that.")
