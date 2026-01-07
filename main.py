from operations import *
from utils import get_num
from matix import Matrix2x2, Matrix3x3
from vectors import Vector
from colorama import Fore, Style

def pause():
    input("\nPress Enter to continue...")

def show_slots(name, slots, color=Fore.WHITE):
    print(f"{Fore.YELLOW}--- {name} Slots ---{Style.RESET_ALL}")
    for i, slot in enumerate(slots):
        label = chr(65 + i)  # A,B,C,D
        if slot is None:
            print(f"{label}: {Fore.RED}Empty{Style.RESET_ALL}")
        else:
            print(f"{label}: {color}Defined{Style.RESET_ALL}")
    print("----------------------")

def basic_calculator():
    while True:
        print(f"\n{Fore.YELLOW}--- Basic Calculator ---{Style.RESET_ALL}")
        print("1. Add  2. Subtract  3. Multiply  4. Divide")
        print("5. Power  6. Root  7. Modulus  8. Exit to Main Menu")
        choice = input("Choose operation: ")
        if choice == '8':
            break
        a = get_num("Enter first number: ")
        b = get_num("Enter second number: ")
        try:
            if choice == '1':
                print(Fore.CYAN, "Result =", add(a, b), Style.RESET_ALL)
            elif choice == '2':
                print(Fore.CYAN, "Result =", subtract(a, b), Style.RESET_ALL)
            elif choice == '3':
                print(Fore.CYAN, "Result =", multiply(a, b), Style.RESET_ALL)
            elif choice == '4':
                print(Fore.CYAN, "Result =", divide(a, b), Style.RESET_ALL)
            elif choice == '5':
                print(Fore.CYAN, "Result =", power(a, b), Style.RESET_ALL)
            elif choice == '6':
                print(Fore.CYAN, "Result =", root(a, b), Style.RESET_ALL)
            elif choice == '7':
                print(Fore.CYAN, "Result =", modulus(a, b), Style.RESET_ALL)
            else:
                print(Fore.RED, "Invalid choice", Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED, "Error:", e, Style.RESET_ALL)
        pause()

def create_matrix2x2():
    return Matrix2x2(
        get_num("a11: "), get_num("a12: "),
        get_num("a21: "), get_num("a22: ")
    )

def matrix2x2_menu(matrices):
    while True:
        show_slots("Matrix 2x2", matrices, color=Fore.BLUE)
        slot = choose_slot()
        print("1. Create / Replace  2. Determinant  3. Transpose  4. Inverse  5. Add with another matrix  6. Exit to Main Menu")
        op = input("Operation: ")
        if op == "6":
            break
        if op == "1":
            matrices[slot] = create_matrix2x2()
            print(Fore.GREEN + "Saved." + Style.RESET_ALL)
        elif matrices[slot] is None:
            print(Fore.RED + "Matrix not defined." + Style.RESET_ALL)
        elif op == "2":
            print(Fore.BLUE, matrices[slot].determinant(), Style.RESET_ALL)
        elif op == "3":
            print(Fore.BLUE, matrices[slot].transpose(), Style.RESET_ALL)
        elif op == "4":
            try:
                print(Fore.BLUE, matrices[slot].inverse(), Style.RESET_ALL)
            except:
                print(Fore.RED + "Singular matrix" + Style.RESET_ALL)
        elif op == "5":
            show_slots("Matrix 2x2", matrices, color=Fore.BLUE)
            slot2 = choose_slot()
            print(Fore.BLUE, matrices[slot] + matrices[slot2], Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid choice" + Style.RESET_ALL)
        pause()

def create_matrix3x3():
    return Matrix3x3(
        get_num("a11: "), get_num("a12: "), get_num("a13: "),
        get_num("a21: "), get_num("a22: "), get_num("a23: "),
        get_num("a31: "), get_num("a32: "), get_num("a33: ")
    )

def matrix3x3_menu(matrices):
    while True:
        show_slots("Matrix 3x3", matrices, color=Fore.BLUE)
        slot = choose_slot()
        print("1. Create / Replace  2. Determinant  3. Transpose  4. Inverse  5. Add with another matrix  6. Exit to Main Menu")
        op = input("Operation: ")
        if op == "6":
            break
        if op == "1":
            matrices[slot] = create_matrix3x3()
            print(Fore.GREEN + "Saved." + Style.RESET_ALL)
        elif matrices[slot] is None:
            print(Fore.RED + "Matrix not defined." + Style.RESET_ALL)
        elif op == "2":
            print(Fore.BLUE, matrices[slot].determinant(), Style.RESET_ALL)
        elif op == "3":
            print(Fore.BLUE, matrices[slot].transpose(), Style.RESET_ALL)
        elif op == "4":
            try:
                print(Fore.BLUE, matrices[slot].inverse(), Style.RESET_ALL)
            except:
                print(Fore.RED + "Singular matrix" + Style.RESET_ALL)
        elif op == "5":
            show_slots("Matrix 3x3", matrices, color=Fore.BLUE)
            slot2 = choose_slot()
            print(Fore.BLUE, matrices[slot] + matrices[slot2], Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid choice" + Style.RESET_ALL)
        pause()

def create_vector():
    dim = input("Vector dimension (2 or 3): ")
    if dim == "2":
        return Vector(get_num("x: "), get_num("y: "))
    else:
        return Vector(get_num("x: "), get_num("y: "), get_num("z: "))

def vector_menu(vectors):
    while True:
        show_slots("Vectors", vectors, color=Fore.GREEN)
        slot = choose_slot()
        print("1. Create / Replace  2. Magnitude  3. Normalize  4. Dot product  5. Cross product  6. Exit to Main Menu")
        op = input("Operation: ")
        if op == "6":
            break
        if op == "1":
            vectors[slot] = create_vector()
            print(Fore.GREEN + "Saved." + Style.RESET_ALL)
        elif vectors[slot] is None:
            print(Fore.RED + "Vector not defined." + Style.RESET_ALL)
        elif op == "2":
            print(Fore.GREEN, vectors[slot].magnitude(), Style.RESET_ALL)
        elif op == "3":
            print(Fore.GREEN, vectors[slot].normalize(), Style.RESET_ALL)
        elif op == "4":
            show_slots("Vectors", vectors, color=Fore.GREEN)
            slot2 = choose_slot()
            print(Fore.GREEN, vectors[slot].dot(vectors[slot2]), Style.RESET_ALL)
        elif op == "5":
            show_slots("Vectors", vectors, color=Fore.GREEN)
            slot2 = choose_slot()
            print(Fore.GREEN, vectors[slot].cross(vectors[slot2]), Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid choice" + Style.RESET_ALL)
        pause()

def choose_slot():
    print("1. A   2. B   3. C   4. D")
    return int(input("Choose slot: ")) - 1

def main():
    matrices2 = [None]*4
    matrices3 = [None]*4
    vectors = [None]*4

    while True:
        print(f"\n{Fore.YELLOW}===== PYTHON CALCULATOR ====={Style.RESET_ALL}")
        print("1. Basic Calculator  2. Matrix 2x2  3. Matrix 3x3  4. Vectors  5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            basic_calculator()
        elif choice == "2":
            matrix2x2_menu(matrices2)
        elif choice == "3":
            matrix3x3_menu(matrices3)
        elif choice == "4":
            vector_menu(vectors)
        elif choice == "5":
            print(Fore.YELLOW + "Goodbye." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
