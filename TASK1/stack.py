class Stack:
    def __init__(self):
        self.items = []


    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False


    def top(self):
        if self.isEmpty():
            print("\nYour stack is empty")
        else:
            return self.items[-1]


    def push(self, value):
        self.items.append(value)


    def pop(self):
        if self.isEmpty():
            print("\nYour stack is empty")
        else:
            value = self.items[len(self.items)-1]
            self.items.pop()
            return value


    def size(self):
        if self.isEmpty():
            print("\nYour stack is empty")
        else:
            return len(self.items)       