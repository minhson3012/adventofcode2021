def main():
    input = readFile("input.txt")
    challenge1Result = challenge1(input)
    print("Challenge 1: ", challenge1Result)
    challenge2Result = challenge2(input)
    print("Challenge 2: ", challenge2Result)


def challenge1(input):
    digitList = []
    for line in input:
        for index, digit in enumerate(line):
            if index + 1 > len(digitList):
                digitList.append({"0": 0, "1": 0})
            if int(digit) == 0:
                digitList[index]["0"] += 1
            elif int(digit) == 1:
                digitList[index]["1"] += 1

    gammaString = ""
    epsilonString = ""
    for index in digitList:
        if index["0"] > index["1"]:
            gammaString += "0"
            epsilonString += "1"
        else:
            gammaString += "1"
            epsilonString += "0"
    return int(gammaString, 2) * int(epsilonString, 2)


def challenge2(input):
    oxygenList = input
    CO2List = input
    index = 0
    while len(oxygenList) > 1:
        oxygenList = parseArray(oxygenList, index, True)
        index += 1

    index = 0
    while len(CO2List) > 1:
        CO2List = parseArray(CO2List, index, False)
        index += 1
    return int(oxygenList[0], 2) * int(CO2List[0], 2)


def parseArray(inputArray, index, keepMajority):
    numOf0 = 0
    numOf1 = 0
    returnList = []
    for input in inputArray:
        if input[index] == "0":
            numOf0 += 1
        else:
            numOf1 += 1

    if keepMajority:
        if (numOf1 > numOf0) or (numOf0 == numOf1):
            for num in inputArray:
                if int(num[index]) == 1:
                    returnList.append(num)
        elif (numOf0 > numOf1):
            for num in inputArray:
                if int(num[index]) == 0:
                    returnList.append(num)
    if not keepMajority:
        if (numOf1 < numOf0):
            for num in inputArray:
                if int(num[index]) == 1:
                    returnList.append(num)
        elif (numOf0 < numOf1) or (numOf0 == numOf1):
            for num in inputArray:
                if int(num[index]) == 0:
                    returnList.append(num)
    return returnList


def readFile(filename):
    file = open(filename, "r")
    inputLines = file.read().splitlines()
    file.close()
    return inputLines


if __name__ == "__main__":
    main()
