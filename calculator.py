print('Do you want 2 or 3 values?')
z = input()
if z == "Is Woo43 the dev?":
    print('Yes.')
elif z == 'two' or z == '2':
        #code for the values
    print("Value 1:"); a = int(input())
    print("Value 2:"); b = int(input())
    print("Choose your operator (+ and plus, -  and minus, * and multiply,  / and divide, = and equals, or square.")
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
    elif op == 'square':
        print('Value 1's square: 'a*a' Value 2's square: 'b*b)
    #else code/error
    else:
        print("Sorry about that. Looks like you made a typo. Try again.")
elif z == 'three' or z == '3':
    #code for the values
    print("Value 1:"); a = int(input())
    print("Value 2:"); b = int(input())
    print("Value 3:"); c = int(input())
    print("Choose your operator (+ or plus, -  or minus, * or multiply,  / or divide, = or cube.")
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
    elif op == "cube":
        print('Value 1's cube: 'a*a*a' Value 2's cube: 'b*b*b' Value 3's cube: 'c*c*c)
    #jokular people error
    else:
        print("Looks like you made a typo. Sorry about that.")
else:
    print("Sorry about that. Looks like you made a typo. Try again.")
