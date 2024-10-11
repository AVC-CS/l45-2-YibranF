import random

def main():
    numbers = []
    total = 0

    while total <= 100:
        num = random.randint(0, 100)  
        numbers.append(num)
        total += num

    print(f"Random numbers generated: {numbers}")
    print(f"Total sum of numbers: {total}")
    

    sum_less_than_100 = sum(num for num in numbers if num < 100)
    print(f"Sum of random numbers less than 100: {sum_less_than_100}")


    return numbers, total


if __name__ == '__main__':
    main()
