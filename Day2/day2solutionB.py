lines = []
sumOfIds = 0

with open('day2input.txt', 'r') as data:
    lines = data.readlines()


def parseLine(line):
    [gameNumber, gameData] = line.split(':')
    print(gameData)
    gameData = gameData.replace(";", ",")
    cubes = gameData.split(",")
    for cube in cubes:
        cube.strip()
    return gameNumber, cubes


def getMinimumsPerGame(cubes):
    MINS = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for cube in cubes:
        print(cube)
        [number, colour] = cube.strip().split(" ")
        if int(number) > int(MINS[colour]):
            MINS[colour] = number
    return MINS


def printGameInfo(gameNumber, sets):
    print('---------------------------------------')
    print(gameNumber)
    print(sets)


for line in lines:
    gameNumber, cubes = parseLine(line)
    minimums = getMinimumsPerGame(cubes)
    powerOfCubes = int(minimums["red"]) * \
        int(minimums["green"])*int(minimums["blue"])
    print(f"Power of cubes for this game is {powerOfCubes}")
    sumOfIds += powerOfCubes
    print(f"Power of cubes added to sum. Sum currently at {sumOfIds}")
print('=======================================')
print(f"final result is {sumOfIds}")
print('=======================================')
