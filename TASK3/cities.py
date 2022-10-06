import numpy as np
import random
from itertools import permutations
from matplotlib import pyplot as plt
from math import dist
from string import ascii_uppercase

def generateCities(number):
    cities = {}
    for i in range(number):
        cities[ascii_uppercase[i]] = (random.randint(-100,100), random.randint(-100,100))
    return cities

def generateConnections(cities, percentage):
    connections = []
    for pair in permutations(cities.keys(), 2):
        if random.randint(0,100) <= percentage:
            connections.append(pair)
    return connections

def printGraph(cities, connections):
    names = list(cities.keys())
    coords = list(cities.values())
    for a,b in connections:
        plt.plot((cities[a][0], cities[b][0]), (cities[a][1], cities[b][1]), 'blue', zorder = 1)
    for i in range(len(cities)):
        plt.scatter(coords[i][0], coords[i][1], c='red', zorder = 2)
        plt.annotate(names[i], (coords[i][0] - 2, coords[i][1] - 10), zorder = 3)
    plt.xlim([-110, 110])
    plt.ylim([-110, 110])
    plt.show()

def generateNextPaths(cities, path, connections):
    nextPaths = []
    for city in cities.keys():
        if city not in path and (path[-1], city) in connections:
            nextPaths.append(path + city)
    return nextPaths

def calcCost(cities, a, b):
   return dist(cities[a], cities[b])

def calcPathCost(cities, path):
    cost = 0
    for a, b in zip(path[:-1], path[1:]):
        cost += calcCost(cities, a, b)
    cost += calcCost(cities, path[-1], path[0])
    return cost

def breadthFirstSearch(cities, startCity, connections):
    paths = [startCity]
    possiblePaths = {}
    while paths:
        currentPath = paths[0]
        nextPaths = generateNextPaths(cities, currentPath, connections)
        if not nextPaths and (currentPath[-1], startCity) in connections and len(currentPath) == len(cities):
            cost = calcPathCost(cities, currentPath + startCity)
            possiblePaths[currentPath + startCity] = round(cost, 2)
        paths.pop(0)
        paths = paths + nextPaths
    if not possiblePaths:
        possiblePaths['No path available'] = 0
        return possiblePaths
    return possiblePaths

def depthFirstSearch(cities, startCity, connections):
    paths = [startCity]
    possiblePaths = {}
    while paths:
        currentPath = paths[0]
        nextPaths = generateNextPaths(cities, currentPath, connections)
        if not nextPaths and (currentPath[-1], startCity) in connections and len(currentPath) == len(cities):
            cost = calcPathCost(cities, currentPath + startCity)
            possiblePaths[currentPath + startCity] = round(cost, 2)
        paths.pop(0)
        paths = nextPaths + paths
    if not possiblePaths:
        possiblePaths['No path available'] = 0
        return possiblePaths
    return possiblePaths

def greedySearch(cities, startCity, connections):
    path = startCity
    while len(path) != len(cities):
        nearestCity = None
        distance = float('inf')
        for newPath in generateNextPaths(cities, path, connections):
            newPathDistance = calcPathCost(cities, newPath[-2:])
            if newPathDistance < distance:
                nearestCity = newPath[-1]
                distance = newPathDistance
        if nearestCity is None:
            return ('', 0)
        path += nearestCity
    if (path[-1], startCity) in connections:
        path += startCity
    else:
        return ('', 0)
    return (path, round(calcPathCost(cities, path), 2))