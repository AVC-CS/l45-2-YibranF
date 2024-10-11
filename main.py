import random


def main():
    total = 0
    numbers = [0] * 5
    for i in range(5):
        while True:
            numbers[i] = random.randint(0,100)
            break

        print(numbers[i], end = ' ')
        total += numbers[i]
    print(total)

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
