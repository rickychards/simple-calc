import math

print("SCIENTIFIC CALCULATOR")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Square Root")
print("7. Sine")
print("8. Cosine")
print("9. Tangent")
print("10. Logarithm")

choice = int(input("Enter your choice: "))

if choice == 1:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    answer = num1 + num2
    print("Answer =", answer)

elif choice == 2:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    answer = num1 - num2
    print("Answer =", answer)

elif choice == 3:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    answer = num1 * num2
    print("Answer =", answer)

elif choice == 4:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num2 == 0:
        print("Cannot divide by zero")
    else:
        answer = num1 / num2
        print("Answer =", answer)

elif choice == 5:
    num1 = float(input("Enter the base: "))
    num2 = float(input("Enter the power: "))
    answer = num1 ** num2
    print("Answer =", answer)

elif choice == 6:
    num = float(input("Enter a number: "))

    if num < 0:
        print("Cannot find square root of a negative number")
    else:
        answer = math.sqrt(num)
        print("Answer =", answer)

elif choice == 7:
    angle = float(input("Enter angle in degrees: "))
    answer = math.sin(math.radians(angle))
    print("Answer =", answer)

elif choice == 8:
    angle = float(input("Enter angle in degrees: "))
    answer = math.cos(math.radians(angle))
    print("Answer =", answer)

elif choice == 9:
    angle = float(input("Enter angle in degrees: "))
    answer = math.tan(math.radians(angle))
    print("Answer =", answer)

elif choice == 10:
    num = float(input("Enter a number: "))

    if num <= 0:
        print("Logarithm is only defined for positive numbers")
    else:
        answer = math.log10(num)
        print("Answer =", answer)

else:
    print("Invalid choice")