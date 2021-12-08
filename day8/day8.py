def main():
    input = readFile("input.txt")
    patterns = []
    outputs = []
    for i in range(0, len(input)):
        splitArray = input[i].split(" | ")
        patterns.append(splitArray[0])
        outputs.append(splitArray[1])
    challenge1Result = challenge1(outputs)
    print("Challenge 1: ", challenge1Result)
    challenge2Result = challenge2(patterns, outputs)
    print("Challenge 2: ", challenge2Result)


def challenge1(outputs):
    uniqueNumbers = 0
    for output in outputs:
        numbers = output.split()
        for num in numbers:
            if len(num) == 2 or len(num) == 4 or len(num) == 3 or len(num) == 7:
                uniqueNumbers += 1
    return uniqueNumbers

# Mark each position of the pattern with numbers:
#        1
#   2         3
#        4
#   5         6
#        7

# Define number patterns based on the position numbers above
pattern0 = [1, 2, 3, 5, 6, 7]
pattern1 = [3, 6]
pattern2 = [1, 3, 4, 5, 7]
pattern3 = [1, 3, 4, 6, 7]
pattern4 = [2, 3, 4, 6]
pattern5 = [1, 3, 4, 5, 7]
pattern6 = [1, 2, 4, 5, 6, 7]
pattern7 = [1, 3, 6]
pattern8 = [1, 2, 3, 4, 5, 6, 7]
pattern9 = [1, 2, 4, 5, 6, 7]

# Crude solution
# Comparing unique numbers with other numbers, examining the difference to determine the number
def challenge2(patterns, outputs):
    totalOutput = 0
    for i in range(0, len(patterns)):
        num1Chars = []
        num4Chars = []
        num7Chars = []
        fiveLinesChars = []
        sixLinesChars = []

        finalNumbers = {}
        for j in range(0, 10):
            finalNumbers[j] = []
        numbers = patterns[i].split()
        # Put the numbers into lists based on their lengths
        for num in numbers:
            if len(num) == 2:
                num1Chars = ([char for char in num])
                finalNumbers[1] = ([char for char in num])
            elif len(num) == 3:
                num7Chars = ([char for char in num])
                finalNumbers[7] = ([char for char in num])
            elif len(num) == 4:
                num4Chars = ([char for char in num])
                finalNumbers[4] = ([char for char in num])
            elif len(num) == 5:
                fiveLinesChars.append([char for char in num])   
            elif len(num) == 6:
                sixLinesChars.append([char for char in num])
            elif len(num) == 7:
                finalNumbers[8] = ([char for char in num])

        # Find the number 0
        for j in range(0, len(sixLinesChars)):
            difference = getDifferentValues(num7Chars, sixLinesChars[j])
            if len(difference) > 0:
                finalNumbers[6] = sixLinesChars[j]
                sixLinesChars.pop(j)
                break

        # Find the number 6, 9
        for j in range(0, len(sixLinesChars)):
            difference = getDifferentValues(num4Chars, sixLinesChars[j])
            if len(difference) > 0:
                finalNumbers[0] = sixLinesChars[j]
            else:
                finalNumbers[9] = sixLinesChars[j]

        # Find the number 3
        for j in range(0, len(fiveLinesChars)):
            difference = getDifferentValues(num1Chars, fiveLinesChars[j])
            if len(difference) == 0:
                finalNumbers[3] = fiveLinesChars[j]
                fiveLinesChars.pop(j)
                break

        # Find the number 2 and 5
        for j in range(0, len(fiveLinesChars)):
            difference = getDifferentValues(num4Chars, fiveLinesChars[j])
            if len(difference) == 1:
                finalNumbers[5] = fiveLinesChars[j]
            else:
                finalNumbers[2] = fiveLinesChars[j]
        
        # Calculate the output
        currentOutput = ""
        outputNums = outputs[i].split()
        for num in outputNums:
            numChars = [char for char in num]
            if len(numChars) == 2:
                currentOutput += '1'
            elif len(numChars) == 3:
                currentOutput += '7'
            elif len(numChars) == 4:
                currentOutput += '4'
            elif len(numChars) == 7:
                currentOutput += '8'
            else:
                for j in finalNumbers:
                    if(len(numChars) == len(finalNumbers[j])):
                        difference = getDifferentValues(numChars, finalNumbers[j])
                        if len(difference) == 0:
                            currentOutput += str(j)
        totalOutput += int(currentOutput)
    return totalOutput

# Get values in listA that are not in listB
def getDifferentValues(listA, listB):
    difference = []
    for element in listA:
        if element not in listB:
            difference.append(element)
    return difference

def readFile(filename):
    file = open(filename, "r")
    inputLines = file.read().splitlines()
    file.close()
    return inputLines


if __name__ == "__main__":
    main()
