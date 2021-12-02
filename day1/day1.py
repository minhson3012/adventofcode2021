def main():
    input = readFile("input.txt")
    challenge1Result = challenge1(input)
    print("Challenge 1: ", challenge1Result)
    challenge2Result = challenge2(input)
    print("Challenge 2: ", challenge2Result)


def challenge1(input):
    lastNum = int(input[0])
    currentNum = int(input[0])
    numOfIncreases = 0
    for line in input:
        currentNum = int(line)
        if currentNum > lastNum:
            numOfIncreases += 1
        lastNum = currentNum
    return numOfIncreases


def challenge2(input):
    numOfIncreases = 0
    for index, line in enumerate(input):
        if index + 2 >= len(input):
            return numOfIncreases
        currentSlidingWindow = int(input[index]) + int(input[index + 1]) + int(input[index + 2])
        lastSlidingWindow = int(input[index - 1]) + int(input[index]) + int(input[index + 1])
        if currentSlidingWindow > lastSlidingWindow:
            numOfIncreases += 1


def readFile(filename):
    file = open(filename, "r")
    inputLines = file.read().splitlines()
    file.close()
    return inputLines


if __name__ == "__main__":
    main()
