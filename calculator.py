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
        print('true')
    elif (a>b):
        print("False, a > b.")
    else:
        print('False, a < b.')
#else code/error
else:
    print("Sorry about that. Looks like you made a typo. Try again.")
