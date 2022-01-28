import art
from os import system
def main():

    def sum (n1, n2):
        return (n1+n2)
    
    def subtract (n1, n2):
        return (n1-n2)
    
    def multiply (n1, n2):
        return n1 * n2
    
    def divide (n1, n2):
        if n2 == 0:
            return "Cannot divide by 0"
        return n1 / n2

    def power (n1, n2):
        return n1 ** n2

    def root (n1, n2):
        return n1 ** (1/n2)
    
    def calculate(n1, operation, n2):
        calculate = {"+" : sum(n1, n2), "-" : subtract(n1, n2), "*" : multiply(n1, n2), "/" : divide(n1, n2), "**" : power(n1, n2), "v" : root(n1, n2)}
        return calculate[operation]

    print(art.logo)
    def calculator():
        answer = "y"
        n1 = float(input("\nWhat is the first number?\nAnswer: "))

        while answer == "y":
            system("cls")
            operation = input("\nWhat is the operation?\nSum -> +\nSubtract -> -\nMultiply -> *\nDivide -> /\nPower -> **\nRoot -> v\nAnswer: ")
            n2 = float(input("\nWhat is the second number?\nAnswer: "))
            result = calculate(n1, operation, n2)
            print(f"{n1} {operation} {n2} = ", result)
            answer = input(f"\nWould you like to continue calculating with {result} as the last calculation result? Type 'y' to continue, or type 'n' to start a new calculation.\nTo stop using the calculator, just type 'exit'\nAnswer: ")

            if answer == "y":
                n1 = result
            elif answer == "exit":
                break
            calculator()

    calculator()
        

if __name__ == '__main__':
    main()