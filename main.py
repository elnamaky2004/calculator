from operations import *
from utils import get_num
import time

def main():
    print("Welcome to the Python Calculator!")
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Root")
        print("7. Modulus")
        print("8. Exit")
        
        choice = input("Enter choice (1-8): ")

        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1','2','3','4','5','6','7']:
            num1 = get_num("Enter first number: ")
            num2 = get_num("Enter second number: ")

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ** {num2} = {power(num1, num2)}")
            elif choice == '6':
                print(f"{num2}-th root of {num1} = {root(num1, num2)}")
            elif choice == '7':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")
        else:
            print("Invalid input. Please enter a number from 1-8.")
        time.sleep(1)    
if __name__ == "__main__":
    main()
