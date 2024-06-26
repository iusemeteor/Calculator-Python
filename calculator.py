def adding():
    first = input("What's the first number you would like to add? ")
    second = input("What's the first number you would like to add? ")
    first = int(first)
    second = int(second)
    answer = first + second
    answer = str(answer)
    print("The answer is " + answer + ".")

def subtract():
    first = input("What's the first number you would like to subtract? ")
    second = input("What's the first number you would like to subtract? ")
    first = int(first)
    second = int(second)
    answer = first - second
    answer = str(answer)
    print("The answer is " + answer + ".")

def multiply():
    first = input("What's the first number you would like to multiply? ")
    second = input("What's the first number you would like to multiply? ")
    first = int(first)
    second = int(second)
    answer = first * second
    answer = str(answer)
    print("The answer is " + answer + ".")

def division():
    first = input("What's the first number you would like to divide? ")
    second = input("What's the first number you would like to divide? ")
    first = int(first)
    second = int(second)
    answer = first / second
    answer = str(answer)
    print("The answer is " + answer + ".")

def main():
    print("Choose a mode:")
    print("1. Adding")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divide")
    option = input("Enter option number: ")
    if option.isdigit():
        option = int(option)
        if option == 1:
            adding()
        elif option == 2:
            subtract()
        elif option == 3:
            multiply()
        elif option == 4:
            division()
    else:
        print("Invalid option!")

if __name__ == '__main__':
    main()
