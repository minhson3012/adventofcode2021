def main():
    input = readFile("input.txt")
    challenge1Result = challenge1(input)
    print("Challenge 1: ", challenge1Result)
    challenge2Result = challenge2(input)
    print("Challenge 2: ", challenge2Result)

# Maybe there's a better way to do this rather than brute forcing
def challenge1(input):
    positionSet = set({})
    for line in input:
        positionSet.add(int(line))

    minFuelUsed = -1
    for pos in positionSet:
        currentFuelUsed = 0
        for line in input:
            currentFuelUsed += abs(pos - int(line))
        if minFuelUsed < 0 or minFuelUsed > currentFuelUsed:
            minFuelUsed = currentFuelUsed
    return minFuelUsed


def challenge2(input):
    positionSet = set({})
    for line in input:
        positionSet.add(int(line))

    minFuelUsed = -1
    for pos in positionSet:
        currentFuelUsed = 0
        for line in input:
            distance = abs(pos - int(line))
            currentFuelUsed += int((distance * (distance + 1))/2)
        if minFuelUsed < 0 or minFuelUsed > currentFuelUsed:
            minFuelUsed = currentFuelUsed
    return minFuelUsed

def readFile(filename):
    file = open(filename, "r")
    inputLines = file.read()
    file.close()
    return inputLines.split(",")


if __name__ == "__main__":
    main()
