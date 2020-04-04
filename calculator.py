print('Do you want 2 or 3 values?')
z = input()
if z == "Is Woo43 the dev?":
    print('Yes.')
elif z == 'two' or z == '2':
        #code for the values
    print("Value 1:"); a = int(input())
    print("Value 2:"); b = int(input())
    print("Choose your operator: + and plus, -  and minus, * and multiply,  / and divide, = and equals, cube a, cube b square a, or square b.")
    #calculation code
    op = input()
    if op == "+" or op == 'plus':
        print(a+b)
    elif op == "-" or op == 'minus':
        print(a-b)
    elif op == "*" or op == 'multiply':
        print(a*b)
    elif op == "/" or op == 'divide':
        print(a/b)
    elif op == "=" or op == 'equals':
        if (a==b):
            print('True.')
        elif (a>b):
            print("False, a > b.")
        else:
            print('False, a < b.')
    elif op == 'square a':
        print(a*a)
    elif op == 'square b':
        print(b*b)
    elif op == "cube a":
        print(a*a*a)
    elif op == "cube b":
        print(b*b*b)
    #else code/error
    else:
        print("Looks like you made a typo. Sorry about that.")
elif z == 'three' or z == '3':
    #code for the values
    print("Value 1:"); a = int(input())
    print("Value 2:"); b = int(input())
    print("Value 3:"); c = int(input())
    print("Choose your operator: + or plus, -  or minus, * or multiply,  / or divide, square a, square b, sqare c, cube a, cube b, or cube c.")
    #calculation code
    op = input()
    if op == "+" or op == 'plus':
        print(a+b+c)
    elif op == "-" or op == 'minus':
        print(a-b-c)
    elif op == "*" or op == 'multiply':
        print(a*b*c)
    elif op == "/" or op == 'divide':
        print(a/b/c)
    elif op == "cube a":
        print(a*a*a)
    elif op == "cube b":
        print(b*b*b)
    elif op == "cube c":
        print(c*c*c)
    elif op == 'square a':
        print(a*a)
    elif op == 'square b':
        print(b*b)
    elif op == 'square c':
        print(c*c)
    #jokular people error
    else:
        print("Looks like you made a typo. Sorry about that.")
else:
    print("Looks like you made a typo. Sorry about that.")
