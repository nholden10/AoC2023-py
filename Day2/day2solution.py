
LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

lines = []
sumOfIds = 0

with open('day2input.txt', 'r') as data:
    lines = data.readlines()


def parseLine(line):
    [gameNumber, gameData] = line.split(':')
    sets = gameData.split(';')
    for set in sets:
        set.strip()
    return gameNumber, sets


def isSetValid(set):
    cubes = set.split(",")
    for cube in cubes:
        [number, colour] = cube.strip().split(" ")
        if int(number) > LIMITS[colour]:
            return False
    return True


def isGameValid(sets):
    for set in sets:
        if isSetValid(set) == False:
            return False
    return True


def printGameInfo(gameNumber, sets):
    print('---------------------------------------')
    print(gameNumber)
    print(sets)


for line in lines:
    gameNumber, sets = parseLine(line)
    printGameInfo(gameNumber, sets)
    if (isGameValid(sets)):
        sumOfIds += int(gameNumber.split(" ")[1])
        print(f"Game is valid. ID added to sum. Sum currently at {sumOfIds}")
    else:
        print("Game is not valid")
print('=======================================')
print(f"final result is {sumOfIds}")
print('=======================================')
