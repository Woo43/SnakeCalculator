print('Do you want 2 or 3 values?')
z = input()
if z == "Is Woo43 the dev":
    print('Yes.')
elif z == 'two' or z == '2':
        #code for the values
    print("Value 1:"); a = int(input())
    print("Value 2:"); b = int(input())
    print("Choose your operator (+ or plus, -  or minus, * or multiply,  / or divide, = or equals.")
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
    #else code/error
    else:
        print("Sorry about that. Looks like you made a typo. Try again.")
elif z == 'three' or z == '3':
    #code for the values
    print("Value 1:"); a = int(input())
    print("Value 2:"); b = int(input())
    print("Value 3:"); c = int(input())
    print("Choose your operator (+ or plus, -  or minus, * or multiply,  / or divide, = or equals.")
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
    #else code/error
    else:
        print("Sorry about that. Looks like you made a typo. Try again.")
else:
    print("Sorry about that. Looks like you made a typo. Try again.")
