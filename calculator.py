print("Do you want 2 or 3 values?")
z = input()
if z == "Am I the dev?":
    print(No.)
if z == 'two':
        #code for the values
    print("Value 1:"); a = int(input())
    print("Value 2:"); b = int(input())
    print("Choose your operator (+, -, *, /, or =).")
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
elif z == '2':
        #code for the values
    print("Value 1:"); a = int(input())
    print("Value 2:"); b = int(input())
    print("Choose your operator (+, -, *, /, or =).")
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
else:
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
