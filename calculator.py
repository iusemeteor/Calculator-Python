def adding():
    while True:
        global first
        global second
        first = input("What's the first number you would like to multiply? ")
        if not first.isdigit():
            print("That's not an integer.")
        else:
            second = input("What's the second number you would like to multiply? ")
            if not second.isdigit():
                print("That's not an integer.")
            else:
                first = int(first)
                second = int(second)
                answer = first + second
                answer = str(answer)
                print("The answer is " + answer + ".")
                exit()
def subtract():
    while True:
        global first
        global second
        first = input("What's the first number you would like to multiply? ")
        if not first.isdigit():
            print("That's not an integer.")
        else:
            second = input("What's the second number you would like to multiply? ")
            if not second.isdigit():
                print("That's not an integer.")
            else:
                first = int(first)
                second = int(second)
                answer = first - second
                answer = str(answer)
                print("The answer is " + answer + ".")
                exit()
def multiply():
    while True:
        global first
        global second
        first = input("What's the first number you would like to multiply? ")
        if not first.isdigit():
            print("That's not an integer.")
        else:
            second = input("What's the second number you would like to multiply? ")
            if not second.isdigit():
                print("That's not an integer.")
            else:
                first = int(first)
                second = int(second)
                answer = first * second
                answer = str(answer)
                print("The answer is " + answer + ".")
                exit()
def division():
    while True:
        global first
        global second
        first = input("What's the first number you would like to divide? ")
        if not first.isdigit():
            print("That's not an integer.")
        else:
            second = input("What's the second number you would like to divide? ")
            if not second.isdigit():
                print("That's not an integer.")
            elif int(second) == 0:
                print("You cannot divide by 0.")
            else:
                first = int(first)
                second = int(second)
                answer = first / second
                answer = str(answer)
                print("The answer is " + answer + ".")
                exit()
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
