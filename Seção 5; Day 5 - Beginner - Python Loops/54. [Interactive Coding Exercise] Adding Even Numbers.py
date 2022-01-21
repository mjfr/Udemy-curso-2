def main():
    #Write your code below this row 👇
    num_sum = 0
    for number in range(1, 101):
        if number % 2 == 0:
            num_sum += number
    print(num_sum)


if __name__ == '__main__':
    main()