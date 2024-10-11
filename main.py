import random


def main():
    total = 0
    numbers = []
    while total <= 100:
            num = random.randint(0,100)
            numbers.append(num)
            print(num, end =' ')
            total += num
    print(f"\nTotal sum: {total}")

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
