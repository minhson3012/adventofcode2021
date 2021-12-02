def main():
    input = readFile("input.txt")
    challenge1Result = challenge1(input)
    print("Challenge 1: ", challenge1Result)
    challenge2Result = challenge2(input)
    print("Challenge 2: ", challenge2Result)


def challenge1(input):
    depth = 0
    horizontalPosition = 0
    for line in input:
        lineList = line.split()
        if lineList[0] == "forward":
            horizontalPosition += int(lineList[1])
        elif lineList[0] == "down":
            depth += int(lineList[1])
        elif lineList[0] == "up":
            depth -= int(lineList[1])
    return depth * horizontalPosition


def challenge2(input):
    depth = 0
    horizontalPosition = 0
    aim = 0
    for line in input:
        lineList = line.split()
        if lineList[0] == "forward":
            horizontalPosition += int(lineList[1])
            depth += int(lineList[1]) * aim
        elif lineList[0] == "down":
            aim += int(lineList[1])
        elif lineList[0] == "up":
            aim -= int(lineList[1])
    return depth * horizontalPosition


def readFile(filename):
    file = open(filename, "r")
    inputLines = file.read().splitlines()
    file.close()
    return inputLines


if __name__ == "__main__":
    main()
