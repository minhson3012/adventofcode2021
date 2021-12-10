def main():
    input = read_file("input.txt")
    challenge1Result = challenge_1(input)
    print("Challenge 1: ", challenge1Result)
    challenge2Result = challenge_2(input)
    print("Challenge 2: ", challenge2Result)

def challenge_1(input):
    points = 0
    for line in input:
        symbols_list = []
        for i in range(0, len(line)):
            if line[i] == "{" or line[i] == "[" or line[i] == "(" or line[i] == "<":
                symbols_list.append(line[i])
            if line[i] == ")":
                if i > 0 and symbols_list[len(symbols_list) - 1] == "(":
                    symbols_list.pop(len(symbols_list) - 1)
                else:
                    points += 3
                    break
            elif line[i] == "]":
                if i > 0 and symbols_list[len(symbols_list) - 1] == "[":
                    symbols_list.pop(len(symbols_list) - 1)
                else:
                    points += 57
                    break
            elif line[i] == "}":
                if i > 0 and symbols_list[len(symbols_list) - 1] == "{":
                    symbols_list.pop(len(symbols_list) - 1)
                else:
                    points += 1197
                    break
            elif line[i] == ">":
                if i > 0 and symbols_list[len(symbols_list) - 1] == "<":
                    symbols_list.pop(len(symbols_list) - 1)
                else:
                    points += 25137
                    break
    return points


def challenge_2(input):
    points_list = []
    for line in input:
        symbols_list = []
        is_incomplete = True
        for i in range(0, len(line)):
            if line[i] == "{" or line[i] == "[" or line[i] == "(" or line[i] == "<":
                symbols_list.append(line[i])
            elif line[i] == ")":
                if i > 0 and symbols_list[len(symbols_list) - 1] == "(":
                    symbols_list.pop(len(symbols_list) - 1)
                else:
                    is_incomplete = False
            elif line[i] == "]":
                if i > 0 and symbols_list[len(symbols_list) - 1] == "[":
                    symbols_list.pop(len(symbols_list) - 1)
                else:
                    is_incomplete = False
            elif line[i] == "}":
                if i > 0 and symbols_list[len(symbols_list) - 1] == "{":
                    symbols_list.pop(len(symbols_list) - 1)
                else:
                    is_incomplete = False
            elif line[i] == ">":
                if i > 0 and symbols_list[len(symbols_list) - 1] == "<":
                    symbols_list.pop(len(symbols_list) - 1)
                else:
                    is_incomplete = False
        if len(symbols_list) == 0:
            is_incomplete = False

        if is_incomplete:
            points = 0
            for i in range(len(symbols_list) - 1, -1, -1):
                points *= 5
                if symbols_list[i] == "(":
                    points += 1
                elif symbols_list[i] == "[":
                    points += 2
                elif symbols_list[i] == "{":
                    points += 3
                elif symbols_list[i] == "<":
                    points += 4
            points_list.append(points)
    
    points_list.sort()
    return points_list[int(len(points_list) / 2)]

def read_file(filename):
    file=open(filename, "r")
    inputLines=file.read().splitlines()
    file.close()
    return inputLines


if __name__ == "__main__":
    main()
