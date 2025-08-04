def addition(a, b):
    result = a + b
    print(result)

def subtraction(a, b):
    result = a - b
    print(result)

def multiplication(a, b):
    result = a * b
    print(result)

def division(a, b):
    result = a / b
    print(result)

def main():
    print('"Welcome to CLI Calculator App"\n')

    while True:
        input1 = input('Enter a number (or type "exit" to quit): ')
        if input1.lower() == 'exit':
            print('Exiting calculator. Thank you!')
            break

        operation = input('Enter operation (+, -, *, /): ')
        if operation.lower() == 'exit':
            print('Exiting calculator. Thank you!')
            break

        input2 = input('Enter second number: ')
        if input2.lower() == 'exit':
            print('Exiting calculator. Thank you!')
            break

        # Convert to float after checking for 'exit'
        try:
            input1 = float(input1)
            input2 = float(input2)
        except ValueError:
            print("Invalid number input! Try again.\n")
            continue

        # Perform the operation
        if operation == '+':
            addition(input1, input2)
        elif operation == '-':
            subtraction(input1, input2)
        elif operation == '*':
            multiplication(input1, input2)
        elif operation == '/':
            if input2 != 0:
                division(input1, input2)
            else:
                print('Cannot divide by zero!')
        else:
            print('Enter a valid operation (+, -, *, /)!')

main()
