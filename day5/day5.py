def main():
    inputLines = readFile("input.txt")
    challenge1Result = challenge1(inputLines)
    print("Challenge 1: ", challenge1Result)
    challenge2Result = challenge2(inputLines)
    print("Challenge 2: ", challenge2Result)

def challenge1(lines):
    pointsDict = {}
    for line in lines:
        startPoint = line[0].split(",")
        endPoint = line[1].split(",")
        if startPoint[0] == endPoint[0] or startPoint[1] == endPoint[1]:
            pointsDict = getHorizontalAndVerticalLines(startPoint, endPoint, pointsDict)
    return sum(value > 1 for value in pointsDict.values())

def challenge2(lines):
    pointsDict = {}
    for line in lines:
        startPoint = line[0].split(",")
        endPoint = line[1].split(",")
        if startPoint[0] == endPoint[0] or startPoint[1] == endPoint[1]:
            pointsDict = getHorizontalAndVerticalLines(startPoint, endPoint, pointsDict)
        elif abs(int(startPoint[0]) - int(endPoint[0])) == abs(int(startPoint[1]) - int((endPoint[1]))):
            pointsDict = getDiagonalLines(startPoint, endPoint, pointsDict)
    return sum(value > 1 for value in pointsDict.values())

# Get horizontal and Diagonal lines
def getHorizontalAndVerticalLines(startPoint, endPoint, dict):
    pointsDict = dict
    startX = int(startPoint[0])
    startY = int(startPoint[1])
    endX = int(endPoint[0])
    endY = int(endPoint[1])
    if startX == endX:
        step = 1 if startY > endY else -1
        for i in range(int(endY), int(startY) + step, step):
            point = str(startX) + "," + str(i)
            if point in pointsDict:
                pointsDict[point] += 1
            else:
                pointsDict[point] = 1
    elif startY == endY:
        step = 1 if startX > endX else -1
        for i in range(int(endX), int(startX) + step, step):
            point = str(i) + "," + str(startY)
            if point in pointsDict:
                pointsDict[point] += 1
            else:
                pointsDict[point] = 1
    return pointsDict

# Get diagonal lines
def getDiagonalLines(startPoint, endPoint, dict):
    pointsDict = dict   
    startX = int(startPoint[0])
    startY = int(startPoint[1])
    endX = int(endPoint[0])
    endY = int(endPoint[1])

    stepX = 1 if startX > endX else -1
    stepY = 1 if startY > endY else -1

    xArray = []
    yArray = []
    for i in range(endX, startX + stepX, stepX):
        xArray.append(i)

    for i in range(endY, startY + stepY, stepY):
        yArray.append(i)

    for i in range(0, len(xArray)):
        point = str(xArray[i]) + "," + str(yArray[i])
        if point in pointsDict:
                pointsDict[point] += 1
        else:
            pointsDict[point] = 1
    return pointsDict

def readFile(filename):
    file = open(filename, "r")
    inputLines = file.read().splitlines()
    file.close()

    parsedLines = []
    for line in inputLines:
        parsedLines.append(line.split(' -> '))
    return parsedLines


if __name__ == "__main__":
    main()