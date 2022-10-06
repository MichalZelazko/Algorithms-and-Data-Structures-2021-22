class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def value(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        lastElement = self.head
        while(lastElement.next):
            lastElement = lastElement.next
        lastElement.next = newNode

    def listPrint(self):
        printingValue = self.head
        while printingValue is not None:
            print(printingValue.data)
            printingValue = printingValue.next