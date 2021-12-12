def main():
    input = read_file("input.txt")
    challenge1Result = challenge_1(input)
    print("Challenge 1: ", challenge1Result)
    challenge2Result = challenge_2(input)
    print("Challenge 2: ", challenge2Result)


def challenge_1(input):
    numbers = []
    for i in range(0, len(input)):
        numbers.append([int(num) for num in input[i]])

    total_flashes = 0
    for i in range(0, 100):
        flashed_points = set({})
        points_to_check = []
        for j in range(0, len(numbers)):
            for k in range(0, len(numbers)):
                if 0 <= numbers[j][k] < 9:
                    numbers[j][k] += 1
                elif numbers[j][k] == 9:
                    numbers[j][k] = 0
                    flashed_points.add(j * 10 + k)
                    points_to_check.append(j * 10 + k)
                    # total_flashes += 1

        while len(points_to_check) > 0:
            currentPoint = points_to_check.pop(0)
            flashed_points, numbers, points_to_check = new_flash(
                flashed_points, numbers, points_to_check, currentPoint)

        total_flashes += len(flashed_points)
    return total_flashes


def challenge_2(input):
    numbers = []
    for i in range(0, len(input)):
        numbers.append([int(num) for num in input[i]])

    all_flashed = False
    num_of_loops = 0
    while not all_flashed:
        num_of_loops += 1
        flashed_points = set({})
        points_to_check = []
        for j in range(0, len(numbers)):
            for k in range(0, len(numbers)):
                if 0 <= numbers[j][k] < 9:
                    numbers[j][k] += 1
                elif numbers[j][k] == 9:
                    numbers[j][k] = 0
                    flashed_points.add(j * 10 + k)
                    points_to_check.append(j * 10 + k)
                    # total_flashes += 1

        while len(points_to_check) > 0:
            currentPoint = points_to_check.pop(0)
            flashed_points, numbers, points_to_check = new_flash(
                flashed_points, numbers, points_to_check, currentPoint)
        if len(flashed_points) == 100:
            all_flashed = True
    return num_of_loops

# I hate this solution


def new_flash(flashed_points, numbers, points_to_check, currentPoint):
    points_to_add = []
    i = int(currentPoint // 10)
    j = currentPoint - i * 10

    if i - 1 >= 0:
        if (0 < numbers[i - 1][j] < 9) or (numbers[i - 1][j] == 0 and ((i - 1) * 10 + j) not in flashed_points):
            numbers[i - 1][j] += 1
        elif numbers[i - 1][j] == 9:
            points_to_add.append((i - 1) * 10 + j)

        if j - 1 >= 0:
            if (0 < numbers[i - 1][j - 1] < 9) or (numbers[i - 1][j - 1] == 0 and ((i - 1) * 10 + j - 1) not in flashed_points):
                numbers[i - 1][j - 1] += 1
            elif numbers[i - 1][j - 1] == 9:
                points_to_add.append((i - 1) * 10 + j - 1)

        if j + 1 < len(numbers):
            if (0 < numbers[i - 1][j + 1] < 9) or (numbers[i - 1][j + 1] == 0 and ((i - 1) * 10 + j + 1) not in flashed_points):
                numbers[i - 1][j + 1] += 1
            elif numbers[i - 1][j + 1] == 9:
                points_to_add.append((i - 1) * 10 + j + 1)

    if i + 1 < len(numbers):
        if (0 < numbers[i + 1][j] < 9) or (numbers[i + 1][j] == 0 and ((i + 1) * 10 + j) not in flashed_points):
            numbers[i + 1][j] += 1
        elif numbers[i + 1][j] == 9:
            points_to_add.append((i + 1) * 10 + j)
        if j - 1 >= 0:
            if (0 < numbers[i + 1][j - 1] < 9) or (numbers[i + 1][j - 1] == 0 and ((i + 1) * 10 + j - 1) not in flashed_points):
                numbers[i + 1][j - 1] += 1
            elif numbers[i + 1][j - 1] == 9:
                points_to_add.append((i + 1) * 10 + j - 1)

        if j + 1 < len(numbers):
            if (0 < numbers[i + 1][j + 1] < 9) or (numbers[i + 1][j + 1] == 0 and ((i + 1) * 10 + j + 1) not in flashed_points):
                numbers[i + 1][j + 1] += 1
            elif numbers[i + 1][j + 1] == 9:
                points_to_add.append((i + 1) * 10 + j + 1)

    if j - 1 >= 0:
        if (0 < numbers[i][j - 1] < 9) or (numbers[i][j - 1] == 0 and (i * 10 + j - 1) not in flashed_points):
            numbers[i][j - 1] += 1
        elif numbers[i][j - 1] == 9:
            points_to_add.append(i * 10 + j - 1)

    if j + 1 < len(numbers):
        if (0 < numbers[i][j + 1] < 9) or (numbers[i][j + 1] == 0 and (i * 10 + j + 1) not in flashed_points):
            numbers[i][j + 1] += 1
        elif numbers[i][j + 1] == 9:
            points_to_add.append(i * 10 + j + 1)

    for point in points_to_add:
        # total_flashes += 1
        currentI = int(point // 10)
        currentJ = point - currentI * 10
        numbers[currentI][currentJ] = 0
        flashed_points.add(point)
        points_to_check.append(point)
    return flashed_points, numbers, points_to_check


def read_file(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()
    return input_lines


if __name__ == "__main__":
    main()
