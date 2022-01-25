def main():
    #Write your code below this line 👇

    def prime_checker(number):
        if number == 2 or number == 3:
            print("It's a prime number.")
        elif (number == 1 or number % 2 == 0 or number % 3 == 0):
            print("It's not a prime number.")
        else:
            print("It's a prime number.")


    #Write your code above this line 👆
        
    #Do NOT change any of the code below👇
    n = int(input("Check this number: "))
    prime_checker(number=n)



if __name__ == '__main__':
    main()