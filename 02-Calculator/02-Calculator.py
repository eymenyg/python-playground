print("Welcome to Python calculator!")
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
print("Enter the operation.\n+ for addition\n- for substraction\n* for multiplication\n/ for division")
opr = input()

result = "undefined"

if opr == '+':
    result = first + second
elif opr == '-':
    result = first - second
elif opr == '*':
    result = first * second
elif opr == '/':
    result = first / second
else:
    print(opr + " is not a correct operation")

print("Result: " + str(result))

print("Bye!")
