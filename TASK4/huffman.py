class Node:
    def __init__(self, value, char, left=None, right=None):
        self.value = value
        self.char = char
        self.left = left
        self.right = right
        self.code = ''
    
    def childrenNodes(self):
        return (self.left, self.right)

    def __str__(self):
        return 'Left child: %s, right child: %s' % (self.left, self.right)

def getProbability(string: str):
    probability = {}
    for char in string:
        if char in list(probability.keys()):
            probability[char] += 1
        else:
            probability[char] = 1
    probability = sorted(probability.items(), key=lambda x: x[1], reverse=True)
    return probability

def makeTree(probability:dict):
    tree = []
    keys = list(probability.keys())
    values = list(probability.values())
    for i in range(len(keys)):
        tree.append(Node(values[i], keys[i]))
    return tree
