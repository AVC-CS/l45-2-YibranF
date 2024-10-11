import random


def main():
    total = 0
    numbers = []
    while total <= 100:
            num = random.randint(1,20)
            numbers.append(num)
            print(num, end =' ')
            total += num
    print(f"\nTotal sum: {total}")
    sum_less_than_100 = sum(num for num in numbers if num < 100)
    print(f"Sum of random numbers less than 100: {sum_less_than_100}")

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
