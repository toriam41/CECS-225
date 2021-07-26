# Tori McDonald
# CECS 225-06
# Lab 2

def andFunction(a, b):
    return a * b

def orFunction(a, b):
    return a + b

def andGate():
    A = int(input("Please enter 1 or 0 for the value of A: "))

    while (A != 1 and A != 0):
        A = int(input("Please enter 1 or 0 for the value of A: "))

    B = int(input("Please enter 1 or 0 for the value of B: "))

    while (B != 1 and B != 0):
        B = int(input("Please enter 1 or 0 for the value of B: "))

    print("A =", A)
    print("B =", B)

    val = andFunction(A, B)

    if (val == 1):
        print(A, "AND", B, "returns 1 (true)")
    else:
        print(A, "AND", B, "returns 0 (false)")

def orGate():
    x = int(input("Please enter 1 or 0 for the value of x: "))

    while (x != 1 and x != 0):
        x = int(input("Please enter 1 or 0 for the value of x: "))

    y = int(input("Please enter 1 or 0 for the value of y: "))

    while (y != 1 and y != 0):
        y = int(input("Please enter 1 or 0 for the value of y: "))

    print("x = ", x)
    print("y = ", y)

    val = orFunction(x, y)

    if (val == 1):
        print(x, " OR ", y, "returns 1 (true)")
    else:
        print(x, " OR ", y, "returns 0 (false)")

def xorGate():
    A = int(input("Please enter 1 or 0 for the value of A: "))

    while (A != 1 and A != 0):
        A = int(input("Please enter 1 or 0 for the value of A: "))

    B = int(input("Please enter 1 or 0 for the value of B: "))

    while (B != 1 and B != 0):
        B = int(input("Please enter 1 or 0 for the value of B: "))

    print("A = ", A)
    print("B = ", B)

    if (A != B):
        print(A, " XOR ", B, "returns 1 (true)")
    else:
        print(A, " XOR ", B, "returns 0 (false)")

def notGate(v):
    if (v == 1):
        opposite = 0
    else:
        opposite = 1

    return opposite

def nandGate():
    A = int(input("Please enter 1 or 0 for the value of A: "))

    while (A != 1 and A != 0):
        A = int(input("Please enter 1 or 0 for the value of A: "))

    B = int(input("Please enter 1 or 0 for the value of B: "))

    while (B != 1 and B != 0):
        B = int(input("Please enter 1 or 0 for the value of B: "))

    print("A = ", A)
    print("B = ", B)

    val = notGate(andFunction(A, B))

    if (val == 1):
        print(A, " NAND ", B, "returns 1 (true)")
    else:
        print(A, " NAND ", B, "returns 0 (false)")

def norGate():
    x = int(input("Please enter 1 or 0 for the value of x: "))

    while (x != 1 and x != 0):
        x = int(input("Please enter 1 or 0 for the value of x: "))

    y = int(input("Please enter 1 or 0 for the value of y: "))

    while (y != 1 and y != 0):
        y = int(input("Please enter 1 or 0 for the value of y: "))

    print("x = ", x)
    print("y = ", y)

    val = notGate(orFunction(x, y))

    if (val == 1):
        print(x, " NOR ", y, "returns 1 (true)")
    else:
        print(x, " NOR ", y, "returns 0 (false)")

def xnorGate():
    A = int(input("Please enter 1 or 0 for the value of A: "))

    while (A != 1 and A != 0):
        A = int(input("Please enter 1 or 0 for the value of A: "))

    B = int(input("Please enter 1 or 0 for the value of B: "))

    while (B != 1 and B != 0):
        B = int(input("Please enter 1 or 0 for the value of B: "))

    print("A = ", A)
    print("B = ", B)

    if (A == B):
        print(A, " XNOR ", B, "returns 1 (true)")
    else:
        print(A, " XNOR ", B, "returns 0 (false)")

def main():
    print("1) AND\n")
    print("2) NAND\n")
    print("3) OR\n")
    print("4) NOR\n")
    print("5) XOR\n")
    print("6) XNOR\n")
    print("7) NOT\n")

    choice = int(input("Please enter below the number of the gate you'd like to select:\n"))

    while (choice < 1 or choice > 7):
        choice = int(input("Please enter one of the valid choices: "))

    if (choice == 1):
        andGate()
    elif (choice == 2):
        nandGate()
    elif (choice == 3):
        orGate()
    elif (choice == 4):
        norGate()
    elif (choice == 5):
        xorGate()
    elif (choice == 6):
        xnorGate()
    else:
        value = int(input("Enter a value (1, 0) for the NOT gate: "))

        while (value != 1 and value != 0):
            value = int(input("Enter a value (1, 0) for the NOT gate: "))

        invert = notGate(value)

        print(value, " NOT returns ", invert)


main()
