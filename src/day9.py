from icecream import ic
from typing import Generator, Any, Tuple, List

from inputFile import inputLines

# https://adventofcode.com/2015/day/9

# type singleSteps = dict[str,dict[str,int]] # {start:{end: distance}}
type SingleSteps =List[List[int]] # steps[start][end] = distance

def getCities(line:str)->Tuple[str,str]:
    idx1 = line.find(" ")
    cityA = line[:idx1]
    idx2 = line.find(" ",idx1+1)
    idx3 = line.find(" ",idx2+1)
    cityB = line[idx2+1:idx3]
    return cityA,cityB

def getDistance(line:str)->int:
    idx = line.find("=")+2
    r = int(line[idx:])
    return r

def addPath(cities:Tuple[int,int], distance:int, steps: SingleSteps)->SingleSteps:
    while len(steps)<max(cities[0],cities[1])+1:
        steps.append([])

    while len(steps[cities[0]])<cities[1]+1:
        steps[cities[0]].append(2^8) # Note dataset maxes < 200

    while len(steps[cities[1]])<cities[0]+1:
        steps[cities[1]].append(2^8) # Note dataset maxes < 200

    steps[cities[0]][cities[1]] = distance
    steps[cities[1]][cities[0]] = distance
    return steps


def cityAlias(city:str,idxToCity:List[str], cityToIdx:dict[str,int])\
                            -> Tuple[List[str], dict[str,int]]:
    if(city in cityToIdx.keys()):
        return idxToCity,cityToIdx

    idxToCity.append(city)
    idx = idxToCity.index(city)
    cityToIdx[city] = idx

    return idxToCity,cityToIdx



def permuteIndices_all(n:int)->List[List[int]]:
    if n <= 0:
        return [[0]]
    # note this is 0 ==> n-1, dealing with n later
    oldPerms = [[0]]
    for i in range(1,n):
        newPerms:List[List[int]] = []
        for perm in oldPerms:
            newPerms += insertM(perm,i)
        oldPerms = newPerms

    # dealing with n
    newPerms = []
    for perm in oldPerms:
        newPerms += insertAfter(1,n,perm)
    return newPerms

def insertM(perm:List[int], m:int)->List[List[int]]:
    r = []
    for i in range(len(perm)+1): # +1 allows appending to the perm
        left = perm[i:]
        right = perm[:i]
        r.append(left+[m]+right)
    return r

def insertAfter(a:int,b:int,perm:List[int])->List[List[int]]:
    """
    @param a: number to be inserted after
    @param b: number to be inserted
    """
    idxA =perm.index(a) # ValueError here if a is poorly defined.
    uptoA = perm[:idxA+1]
    afterA = perm[idxA+1:]
    all = insertM(afterA,b)
    r = []

    for perm in all:
        r.append(uptoA + perm)
    return r


def fullPathLength(path:List[int],distances:SingleSteps):
    dist = 0
    indices = len(path)-1
    for idx in range(indices):
        CityA = path[idx]
        CityB = path[idx+1]
        dist += distances[CityA][CityB]
    return dist



def part1(lines: Generator[str, Any, None]):
    # Note that the brute force method will calculate all possible paths which gives n!, with reversible directions this is n!/2.
    # In this case 8!/2 = 20160
    # This is doable

    # Note: to remove half the paths we can just say that the first city in the list if Always visited before the last city.
    # Blah blah combinatorics...trivial.


    citySet = set({})
    cityList = []
    cityDict = {}
    distances:SingleSteps = []



    for line in lines:
        CityA, CityB = getCities(line)

        citySet.add(CityA)
        citySet.add(CityB)

        cityList,cityDict = cityAlias(CityA,cityList,cityDict)
        cityList,cityDict = cityAlias(CityB,cityList,cityDict)

        distance = getDistance(line)

        idxA = cityDict[CityA]
        idxB = cityDict[CityB]

        distances = addPath((idxA, idxB),distance, distances)
        pass

    allPerms = permuteIndices_all(len(cityList))

    r = []

    for perm in allPerms:
        r.append(fullPathLength(perm,distances))
    return min(r)
    pass


def part2(lines: Generator[str, Any, None]):
    for line in lines:
        pass
    pass


if __name__ == "__main__":
    lines = inputLines(9)
    print("part 1: ", part1(lines))
    lines2 = inputLines(9)
    print("part 2: ", part2(lines2))
    pass
