def main():
    input = readFile("input.txt")
    dayDict = {}
    for i in range(0, 9):
        dayDict[i] = 0

    for item in input:
        if int(item) in dayDict:
            dayDict[int(item)] += 1
    challenge1Result = challenge(dayDict, 80)
    print("Challenge 1: ", challenge1Result)
    challenge2Result = challenge(dayDict, 256)
    print("Challenge 2: ", challenge2Result)
'''
Looping through a massive list for 80 times is not a good idea, 
especially when the amount of times looped can increase.
Use a dictionary instead and count the number of times a number appears
'''
def challenge(input, times):
    currentDayDict = dict(input)
    for i in range(0, times):
        newDayDict = dict(currentDayDict)
        for j in range(8, -1, -1):
            if j == 8:
                newDayDict[7] = currentDayDict[8]
                newDayDict[8] = 0
            elif j == 0:
                newDayDict[6] += currentDayDict[0]
                newDayDict[8] = currentDayDict[0]
            else:
                newDayDict[j - 1] = currentDayDict[j]
        currentDayDict = dict(newDayDict)
    
    totalFish = 0
    for day in currentDayDict:
        totalFish += currentDayDict[day]
    return totalFish

def readFile(filename):
    file = open(filename, "r")
    inputLines = file.read()
    file.close()
    return inputLines.split(",")


if __name__ == "__main__":
    main()
