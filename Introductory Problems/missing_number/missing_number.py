import timeit
from statistics import mean


def algorithm(first_line, second_line):
    max_number = first_line
    numbers = {int(i) for i in second_line.split()}

    for i in range(1, int(max_number) + 1):
        if i not in numbers:
            return i


def algorithm2(first_line, second_line):
    all_numbers = set(range(1, int(first_line) + 1))
    numbers = {int(i) for i in second_line.split()}

    [missing_number] = all_numbers - numbers

    return missing_number


def algorithm3(first_line, second_line):
    first_line = int(first_line)
    all_numbers = (first_line * (first_line + 1)) // 2
    numbers = [int(i) for i in second_line.split()]

    missing_number = all_numbers - sum(numbers)

    return missing_number


def algorithm4(first_line, second_line):
    first_line = int(first_line)
    all_numbers = (first_line * (first_line + 1)) // 2
    numbers = map(int, second_line.split())

    missing_number = all_numbers - sum(numbers)

    return missing_number


def algorithm5(first_line, second_line):
    first_line = int(first_line)
    all_numbers = (first_line * (first_line + 1)) // 2
    numbers = sum(int(i) for i in second_line.split())

    missing_number = all_numbers - numbers

    return missing_number


if __name__ == "__main__":
    with open(r"test_case.txt", encoding="utf-8") as file:
        first_line = file.readline()
        second_line = file.readline()

    t = timeit.repeat(lambda: algorithm(first_line, second_line), number=1, repeat=50)
    print(mean(t))

    t = timeit.repeat(lambda: algorithm2(first_line, second_line), number=1, repeat=50)
    print(mean(t))

    t = timeit.repeat(lambda: algorithm3(first_line, second_line), number=1, repeat=50)
    print(mean(t))

    t = timeit.repeat(lambda: algorithm4(first_line, second_line), number=1, repeat=50)
    print(mean(t))

    t = timeit.repeat(lambda: algorithm5(first_line, second_line), number=1, repeat=50)
    print(mean(t))
