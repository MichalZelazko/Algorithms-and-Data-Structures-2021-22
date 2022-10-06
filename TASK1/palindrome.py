from stack import Stack
from linkedList import *

def puttingInList(list, inputString):
    for char in inputString:
        list.insert(char)


def puttingOnStack(stack, inputString):
    for char in inputString:
        stack.push(char)


def isPalindrome(stack, list):
    if list.head is None:
        print("\nYour string is empty")
        return
    else:
        char = list.head
        while char is not None:
            if char.data == stack.pop():
                char = char.next
            else:
                return False
        return True


def main():
    list = LinkedList()
    stack = Stack()
    inputString = input("Insert the string you want to check: ")
    puttingInList(list, inputString)
    puttingOnStack(stack, inputString)
    if isPalindrome(stack, list):
        print("\nYour string is a palindrome")
    else:
        print("\nYour string is not a palindrome")

if __name__ == "__main__":
    main()