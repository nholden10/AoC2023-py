with open('day1input.txt', 'r') as data:
    lines = data.readlines()
    print(lines)

    Nums = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    def reverse(str):
        return str[::-1]

    def replanceNums(line):
        lowestIndex = len(line)
        swapNum = ""
        for num in Nums:
            if (num in line):
                index = line.find(num)
                if (index < lowestIndex):
                    lowestIndex = index
                    swapNum = num
            else:
                continue
        if swapNum != "":
            newline = line.replace(swapNum, str(Nums[swapNum]))
        else:
            newline = line
        return newline

    def reverseReplaceNums(line):
        reversedLine = reverse(line)
        lowestIndex = len(line)
        swapNum = ""
        for num in Nums:
            reversedKey = reverse(num)
            if (reversedKey in reversedLine):
                index = reversedLine.find(reversedKey)
                if (index < lowestIndex):
                    lowestIndex = index
                    swapNum = reversedKey
            else:
                continue
        if swapNum != "":
            newline = reversedLine.replace(
                swapNum, str(Nums[reverse(swapNum)]))
            newerline = reverse(newline)
        else:
            newerline = line
        return newerline

    def findNumberFromStart(line):
        for char in line:
            if (char.isnumeric()):
                return char
            else:
                continue

    def findNumberFromEnd(line):
        for char in reverse(line):
            if (char.isnumeric()):
                return char
            else:
                continue

    total = 0

    for line in lines:
        print("-----------------------------------------------")
        print("Starting line:", line)
        replacedLine = replanceNums(line)
        reversedReplacedLine = reverseReplaceNums(replacedLine)
        print("Line after replacements:", reversedReplacedLine)
        number = findNumberFromStart(
            reversedReplacedLine) + findNumberFromEnd(reversedReplacedLine)
        print("Number:", number)
        total += int(number)
        print("Accumulated Total:", total)
    print(f"Total sum is {total}")
