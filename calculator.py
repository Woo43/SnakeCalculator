z = input("Do you want 2 or 3 values?: ").lower()
if z in ("two", "2", "dos", "1+1"):
    how_many = 2
    print("You've picked: two values")
else:
    how_many = 3
    print("You've picked: three values")

while True:
    try:
        a = int(input("Value 1: "))
        break
    except ValueError:
        print("Sorry about that. Looks like you made a typo. Try again.")
while True:
    try:
        b = int(input("Value 2: "))
        continue_it = True
        break
    except ValueError:
        print("Sorry about that. Looks like you made a typo. Try again.")
    
if continue_it:
    if how_many == 3:
        while True:
            try:
                c = int(input("Value 3: "))
                break
            except ValueError:
                print("Sorry about that. Looks like you made a typo. Try again.")
    op = input("Choose your operator (plus, minus, multiply, divide, or equals): ")
    #calculation code
    if op in ("plus", "+"):
        if how_many == 2:
            print(a+b)
        else:
            print(a+b+c)
    elif op in ("minus", "-"):
        if how_many == 2:
            print(a-b)
        else:
            print(a-b-c)
    elif op in ("multiply", "*"):
        if how_many == 2:
            print(a*b)
        else:
            print(a*b*c)
    elif op in ("divide", "/"):
        if how_many == 2:
            print(a/b)
        else:
            print(a/b/c)
    elif op in ("equals", "="):
        if how_many == 2:
            if (a==b):
                print("True.")
            elif (a>b):
                print("False, a > b.")
            else:
                print("False, a < b.")
        else:
            print("Sorry about that. Looks like you made a typo. Try again.")
    else:
        print("Sorry about that. Looks like you made a typo. Try again.")
