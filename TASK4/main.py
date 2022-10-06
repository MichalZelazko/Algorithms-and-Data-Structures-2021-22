from huffman import *

def main():
    text = "I love data structures"
    probability = getProbability(text)
    print(probability)
    tree = makeTree(probability)
    print(tree)

if __name__ == "__main__":
    main()