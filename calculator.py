#code for the values
print("Value 1:")
a = int(input())
print("Value 2:")
b = int(input())
print("Choose your operator (plus, minus, multiply, or divide).")
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
#else code/error
else:
    print("Oops. You made a typo.")