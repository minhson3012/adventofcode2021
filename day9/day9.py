def main():
    input = read_file("input.txt")
    challenge1Result = challenge_1(input)
    print("Challenge 1: ", challenge1Result)
    challenge2Result = challenge_2(input)
    print("Challenge 2: ", challenge2Result)


def challenge_1(input):
    total_risk_level = 0
    skippable_points = []
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            is_low_point = True
            if (i * len(input) + j) in skippable_points:
                continue
            if (((i - 1 >= 0) and input[i - 1][j] < input[i][j]) or 
                (j - 1 >= 0) and input[i][j - 1] < input[i][j]):
                is_low_point = False
            if (j + 1 < len(input[i])):
                if input[i][j + 1] > input[i][j]:
                    skippable_points.append(i * len(input) + (j + 1))
                else:
                    is_low_point = False
            if (i + 1 < len(input)):
                if input[i + 1][j] > input[i][j]:
                    skippable_points.append((i + 1) * len(input) + j)
                else:
                    is_low_point = False
            if is_low_point:
                total_risk_level += 1 + int(input[i][j])
    return total_risk_level


def challenge_2(input):
    skippable_points = []
    basins_list = []
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            is_low_point = True
            if (i * len(input) + j) in skippable_points:
                continue
            if (((i - 1 >= 0) and input[i - 1][j] < input[i][j]) or 
                (j - 1 >= 0) and input[i][j - 1] < input[i][j]):
                is_low_point = False
            if (j + 1 < len(input[i])):
                if input[i][j + 1] > input[i][j]:
                    skippable_points.append(i * len(input) + (j + 1))
                else:
                    is_low_point = False
            if (i + 1 < len(input)):
                if input[i + 1][j] > input[i][j]:
                    skippable_points.append((i + 1) * len(input) + j)
                else:
                    is_low_point = False
            if is_low_point:
                basins_list.append(get_basin_size(input, i, j))
    
    basins_list.sort(reverse=True)
    return basins_list[0] * basins_list[1] * basins_list[2]


def get_basin_size(input, i, j):
    basin_points_list = set({i * len(input) + j})
    check_points_list = []
    checked_points_list = set({i * len(input) + j})

    basin_points_list, check_points_list = add_to_lists(input, i, j, basin_points_list, check_points_list)
    
    while len(check_points_list) > 0:
        currentPoint = check_points_list.pop(len(check_points_list) - 1)
        if currentPoint in checked_points_list:
            continue
        checked_points_list.add(currentPoint)
        currentI = currentPoint // len(input)
        currentJ = currentPoint - currentI * len(input)
        basin_points_list, check_points_list = add_to_lists(input, currentI, currentJ, basin_points_list, check_points_list)

    return len(basin_points_list)

def add_to_lists(input, i, j, basin_points_list, check_points_list):
    points_list = []
    if i - 1 >= 0 and input[i - 1][j] > input[i][j] and input[i - 1][j] != '9':
        points_list.append((i - 1) * len(input) + j)
    if j - 1 >= 0 and input[i][j - 1] > input[i][j] and input[i][j - 1] != '9':
        points_list.append(i * len(input) + j - 1)
    if i + 1 < len(input) and input[i + 1][j] > input[i][j] and input[i + 1][j] != '9':
        points_list.append((i + 1) * len(input) + j)
    if j + 1 < len(input[i]) and input[i][j + 1] > input[i][j] and input[i][j + 1] != '9':
        points_list.append(i * len(input) + j + 1)

    for value in points_list:
        basin_points_list.add(value)
        if value not in check_points_list:
            check_points_list.append(value)
    return basin_points_list, check_points_list


def read_file(filename):
    file=open(filename, "r")
    inputLines=file.read().splitlines()
    file.close()
    return inputLines


if __name__ == "__main__":
    main()
