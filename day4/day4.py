def main():
    inputNumbers, bingoBoards = readFile("input.txt")
    challenge1Result = challenge1(inputNumbers, bingoBoards)
    print("Challenge 1: ", challenge1Result)
    challenge2Result = challenge2(inputNumbers, bingoBoards)
    print("Challenge 2: ", challenge2Result)

def challenge1(inputNumbers, bingoBoards):
    bingoBoardsStatus = []
    for i in range(0, len(bingoBoards)):
        bingoBoardsStatus.append([])

    for i in range(0, len(inputNumbers)):
        for j in range(0, len(bingoBoards)):
            if inputNumbers[i] in bingoBoards[j]:
                numberIndex = bingoBoards[j].index(inputNumbers[i])
                if numberIndex not in bingoBoardsStatus[j]:
                    bingoBoardsStatus[j].append(numberIndex)
                    bingoBoardsStatus[j].sort()
                    if isBingo(bingoBoardsStatus[j]):
                        return int(inputNumbers[i]) * sumOfUnmarked(bingoBoardsStatus[j], bingoBoards[j])

    return 0

def challenge2(inputNumbers, bingoBoards):
    bingoBoardsStatus = []
    for i in range(0, len(bingoBoards)):
        bingoBoardsStatus.append([])

    lastWinningBingoIndex = 0
    lastWinningDrawNumber = 0
    winningBingoBoards = []
    for i in range(0, len(inputNumbers)):
        for j in range(0, len(bingoBoards)):
            if inputNumbers[i] in bingoBoards[j] and j not in winningBingoBoards:
                numberIndex = bingoBoards[j].index(inputNumbers[i])
                if numberIndex not in bingoBoardsStatus[j]:
                    bingoBoardsStatus[j].append(numberIndex)
                    bingoBoardsStatus[j].sort()
                    if isBingo(bingoBoardsStatus[j]):
                        lastWinningBingoIndex = j
                        lastWinningDrawNumber = i
                        winningBingoBoards.append(j)
    return int(inputNumbers[lastWinningDrawNumber]) * sumOfUnmarked(bingoBoardsStatus[lastWinningBingoIndex], bingoBoards[lastWinningBingoIndex])

# Check for every possible bingo winning condition in the crudest way possible
def isBingo(status):
    if len(status) < 5:
        return False

    # Can I do this when I already know that bingo boards are 5x5?
    for i in range(0, 5):
        # Column check
        if i in status and i + 5 in status and i + 10 in status and i + 15 in status and i + 20 in status:
            return True
        j = i * 5
        # Row check
        if j in status and j + 1 in status and j + 2 in status and j + 3 in status and j + 4 in status:
                return True
    return False

def sumOfUnmarked(bingoBoardStatus, bingoBoard):
    sumOfUnmarked = 0
    for i in range(0, len(bingoBoard)):
        if i not in bingoBoardStatus:
            sumOfUnmarked += int(bingoBoard[i])
    return sumOfUnmarked

def readFile(filename):
    file = open(filename, "r")
    inputLines = file.read().splitlines()
    file.close()

    inputNumbers = inputLines[0].split(',')
    bingoBoards = []
    currentIndex = 0
    for i in range(2, len(inputLines)):
        if not inputLines[i]:
            currentIndex += 1
        else:
            if currentIndex + 1 > len(bingoBoards):
                bingoBoards.append([])
            
            # Print each board as a single list
            bingoBoards[currentIndex] += inputLines[i].split()
    return inputNumbers, bingoBoards


if __name__ == "__main__":
    main()
