def algorithm(n):
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

    print("1", end="")


if __name__ == "__main__":
    n = int(input())
    algorithm(n)
