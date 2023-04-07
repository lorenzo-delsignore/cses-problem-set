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
    max_number = int(first_line)
    sum_all_numbers = (max_number * (max_number + 1)) // 2
    numbers = [int(i) for i in second_line.split()]

    missing_number = sum_all_numbers - sum(numbers)

    return missing_number


def algorithm4(first_line, second_line):
    max_number = int(first_line)
    sum_all_numbers = (max_number * (max_number + 1)) // 2
    numbers = map(int, second_line.split())

    missing_number = sum_all_numbers - sum(numbers)

    return missing_number


def algorithm5(first_line, second_line):
    max_number = int(first_line)
    sum_all_numbers = (max_number * (max_number + 1)) // 2
    numbers = sum(int(i) for i in second_line.split())

    missing_number = sum_all_numbers - numbers

    return missing_number


if __name__ == "__main__":
    with open(r"test_case.txt", encoding="utf-8") as file:
        first_line = file.readline()
        second_line = file.readline()

    algorithms = [algorithm, algorithm2, algorithm3, algorithm4, algorithm5]
    for algo in algorithms:
        t = timeit.repeat(lambda: algo(first_line, second_line), number=1, repeat=50)
        print(mean(t))
