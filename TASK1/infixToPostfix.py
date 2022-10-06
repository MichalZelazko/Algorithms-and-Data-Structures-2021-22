from stack import Stack


def menu():
    print("\n1. Add another element to your stack")
    print("2. Remove the top element of your stack")
    print("3. Show the top element of your stack")
    print("4. Show the number of elements of your stack")
    print("5. Exit")


def stackExample():
    stack = Stack()
    while True:
        menu()
        menu_choice = input("Your choice: ")
        if menu_choice == 1:
            value = input("\nAdd a new element to your stack: ")
            stack.push(value)
        elif menu_choice == 2:
            print(f" Element popped from your stack is {stack.pop()}")
        elif menu_choice == 3:
            print(f" Top element of your stack is {stack.top()}")
        elif menu_choice == 4:
            print(f"\nYou have {stack.size()} elements on your stack.")
        elif menu_choice == 5:
            return False
        else:
            print("\nYour choice must be one of the numbers visible \
                  in the menu! Choose again!")


def isNumber(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def toPostfix(infix):
    precedence = {'*': 1, '/': 1, '+': 2, '-': 2, '(': 3, ')': 3}
    possibleOperators = ['+', '-', '/', '*']
    operators = Stack()
    expression = infix.split()
    postfix = ""
    for char in expression:
        if isNumber(char):
            postfix += char + ' '
        else:
            if operators.isEmpty():
                operators.push(char)
            elif char in possibleOperators:
                while (not operators.isEmpty() and operators.top() not in '()' and
                       not precedence[char] > precedence[operators.top()]):
                    postfix += operators.pop() + ' '
                operators.push(char)
            elif char == '(':
                operators.push(char)
            elif char == ')':
                while (not operators.isEmpty() and operators.top() != '('):
                    postfix += operators.pop() + ' '
                operators.pop()
    while not operators.isEmpty():
        postfix += operators.pop() + ' '
    return postfix


def postfixCalculation(postfix):
    result = 0
    calcStack = Stack()
    expression = postfix.split()
    for char in expression:
        if isNumber(char):
            calcStack.push(char)
        else:
            if calcStack.size() >= 2:
                value2 = float(calcStack.pop())
                value1 = float(calcStack.pop())
            else:
                return False
            if char == '+':
                result = value1 + value2
            elif char == '-':
                result = value1 - value2
            elif char == '*':
                result = value1 * value2
            elif char == '/':
                result = value1 / value2
            else:
                print("Unexpected operator!")
            calcStack.push(result)
    result = calcStack.pop()
    if calcStack.isEmpty():
        return result
    else:
        return False

def main():
    infix = input("Enter your expression in infix notation: ")
    postfix = toPostfix(infix)
    print(f"In infix: {infix}\nIn postfix: {postfix}")
    if postfixCalculation(postfix):
        print(f"Result of that expression is {postfixCalculation(postfix)}")
    else:
        print("Your expression is incorrect")


if __name__ == "__main__":
    main()
