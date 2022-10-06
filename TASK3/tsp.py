from cities import *

NUMBER_OF_CITIES = 5

def main():
    cities = generateCities(NUMBER_OF_CITIES)
    connections = generateConnections(cities, 100)

    print("Cities: ", cities)
    print("\nConnections: ", connections)

    paths = breadthFirstSearch(cities, 'A', connections)
    print("\nBreadth first search:\n-------------------------\nAll paths: ", paths)
    if 'No path available' in list(paths.keys()):
        print("No path was found")
    else:
        shortestPath = min(paths.items(), key = lambda path: path[1])
        print("---------------\nThe best path: ", shortestPath)

    paths.clear()
    paths = depthFirstSearch(cities, 'A', connections)
    print("\nDepth first search:\n-------------------------\nAll paths: ", paths)
    if 'No path available' in list(paths.keys()):
        print("No path was found")
    else:
        shortestPath = min(paths.items(), key = lambda path: path[1])
        print("---------------\nThe best path: ", shortestPath)

    print("\nGreedy search:\n-------------------------\nThe best path: ", greedySearch(cities, 'A', connections))
    printGraph(cities, connections)

if __name__ == "__main__":
    main()
