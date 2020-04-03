import sys
from io import StringIO
newin = StringIO("2\n1\n2\nplus\n")
sys.stdin = newin

def get_input():
    try:
        return input()
    except EOFError:
        return None

print("Do you want 2 or 3 values?")
z = get_input()
if z == 'two' or z == '2':
    #code for the values
    print("Value 1:"); a = int(get_input())
    print("Value 2:"); b = int(get_input())
    print("Choose your operator (+, -, *, /, or =).")
    #calculation code
    op = get_input()
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
else:
    #code for the values
    print("Value 1:"); a = int(get_input())
    print("Value 2:"); b = int(get_input())
    print("Value 3:"); c = int(get_input())
    print("Choose your operator (+, -, *, or ,).")
    #calculation code
    op = get_input()
    if op == "+":
        print(a+b+c)
    elif op == "-":
        print(a-b-c)
    elif op == "*":
        print(a*b*c)
    elif op == ",":
        print(a/b/c)
    #else code/error
    else:
        print("Sorry about that. Looks like you made a typo. Try again.")
