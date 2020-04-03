print("Do you want 2 or 3 values?")
z = input()
if z == 'two':
    #code for the values
    print("Value 1:"); a = int(input())
    print("Value 2:"); b = int(input())
    print("Choose your operator (plus, minus, multiply, divide, or equals).")
    #calculation code
    op = input()
    if op == "plus":
        print(a+b)
    elif op == "minus":
        print(a-b)
    elif op == "multiply":
        print(a*b)
    elif op == "divide":
        print(a/b)
    elif op == "equals":
        if (a==b):
            print('True.')
        elif (a>b):
            print("False, a > b.")
        else:
            print('False, a < b.')
    #else code/error
    else:
        print("Sorry about that. Looks like you made a typo. Try again.")
elif z == '2':
        #code for the values
    print("Value 1:"); a = int(input())
    print("Value 2:"); b = int(input())
    print("Choose your operator (plus, minus, multiply, divide, or equals).")
    #calculation code
    op = input()
    if op == "plus":
        print(a+b+c)
    elif op == "minus":
        print(a-b-c)
    elif op == "multiply":
        print(a*b*c)
    elif op == "divide":
        print(a/b/c)
    elif op == "equals":
        if (a==b):
            print('True.')
        elif (a>b):
            print("False, a > b.")
        else:
            print('False, a < b.')
    #else code/error
    else:
        print("Sorry about that. Looks like you made a typo. Try again.")
else:
    #code for the values
    print("Value 1:"); a = int(input())
    print("Value 2:"); b = int(input())
    print("Value 3:"); c = int(input())
    print("Choose your operator (plus, minus, multiply, or divide).")
    #calculation code
    op = input()
    if op == "plus":
        print(a+b+c)
    elif op == "minus":
        print(a-b-c)
    elif op == "multiply":
        print(a*b*c)
    elif op == "divide":
        print(a/b/c)
    #else code/error
    else:
        print("Sorry about that. Looks like you made a typo. Try again.")
