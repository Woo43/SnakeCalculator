print('Do you want 2 or 3 values?')
z = input()
if z == "Is Woo43 the dev":
    print('Yes.')
if z == 'two' or "2":
        #code for the values
    print("Value 1:"); a = int(input())
    print("Value 2:"); b = int(input())
    print("Choose your operator (+, -, *, /, or =).")
    #calculation code
    op = input()
    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a/b)
    elif op == "=":
        if (a==b):
            print('True.')
        elif (a>b):
            print("False, a > b.")
        else:
            print('False, a < b.')
    #else code/error
    else:
        print("Sorry about that. Looks like you made a typo. Try again.")
elif z == 'three' or '3':
    #code for the values
    print("Value 1:"); a = int(input())
    print("Value 2:"); b = int(input())
    print("Value 3:"); c = int(input())
    print("Choose your operator (+, -, *, or /).")
    #calculation code
    op = input()
    if op == "+":
        print(a+b+c)
    elif op == "-":
        print(a-b-c)
    elif op == "*":
        print(a*b*c)
    elif op == "/":
        print(a/b/c)
    #else code/error
    else:
        print("Sorry about that. Looks like you made a typo. Try again.")
else:
    print("Sorry about that. Looks like you made a typo. Try again.")
