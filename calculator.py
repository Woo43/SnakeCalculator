#code for the values
print("Value 1:"); a = int(input())
print("Value 2:"); b = int(input())
print("Value 3:"); c = int(input())
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
