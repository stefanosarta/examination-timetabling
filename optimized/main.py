"""
Stefanos Moungkoulis
21/01/2021
Project of UOI

GitHub Page: https://github.com/stefanosarta/examination-timetabling
Markdown Page: https://stefanosarta.github.io/examination-timetabling/

"""

from load_problem import load_problem
from solve_problem import solve_problem
from load_solution import load_solution
from load_solution import mass_solve
from optimize import optimize_problem
"""
Load functions from other files
Theese functions will be called after user has selected each of the choices
"""


files_names = ["car-f-92.stu", "car-s-91.stu", "ear-f-83.stu",
               "hec-s-92.stu", "kfu-s-93.stu", "lse-f-91.stu",
               "pur-s-93.stu", "rye-s-93.stu", "sta-f-83.stu",
               "tre-s-92.stu", "uta-s-92.stu", "ute-s-92.stu",
               "yor-f-83.stu"]

solution_names = ["car-f-92.sol", "car-s-91.sol", "ear-f-83.sol",
                  "hec-s-92.sol", "kfu-s-93.sol", "lse-f-91.sol",
                  "pur-s-93.sol", "rye-s-93.sol", "sta-f-83.sol",
                  "tre-s-92.sol", "uta-s-92.sol", "ute-s-92.sol",
                  "yor-f-83.sol", "car-f-92.sol2"]


def menu():
    """ Function for the available choices. """
    print("[1] Load a problem")
    print("[2] Solve a problem")
    print("[3] Load a solution")
    print("[4] Mass solve all the problems")
    print("[5] Optimize the problem that was just solved")
    print("[0] Exit the Programm")


def files():
    """ Function for the available files. """
    files = (["[1] car-f-92.stu", "[2] car-s-91.stu", "[3] ear-f-83.stu",
              "[4] hec-s-92.stu", "[5] kfu-s-93.stu", "[6] lse-f-91.stu",
              "[7] pur-s-93.stu", "[8] rye-s-93.stu", "[9] sta-f-83.stu",
              "[10] tre-s-92.stu", "[11] uta-s-92.stu", "[12] ute-s-92.stu",
              "[13] yor-f-83.stu"])

    for x in range(len(files)):
        print(files[x])


def solutions():
    """ Function for the available solution files. """
    solutions = (["[1] car-f-92.sol", "[2] car-s-91.sol", "[3] ear-f-83.sol",
                  "[4] hec-s-92.sol", "[5] kfu-s-93.sol", "[6] lse-f-91.sol",
                  "[7] pur-s-93.sol", "[8] rye-s-93.sol", "[9] sta-f-83.sol",
                  "[10] tre-s-92.sol", "[11] uta-s-92.sol",
                  "[12] ute-s-92.sol", "[13] yor-f-83.sol"])

    for x in range(len(solutions)):
        print(solutions[x])


menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        files()
        print(" ")
        print("Select number of the file")
        option2 = int(input("Enter file number: "))
        load_problem(files_names[option2-1])

    elif option == 2:
        files()
        print(" ")
        print("Select number of the file")
        option2 = int(input("Enter file number: "))
        solve_problem(files_names[option2-1])

    elif option == 3:
        solutions()
        print(" ")
        print("Select number of the file")
        option2 = int(input("Enter file number: "))
        load_solution(solution_names[option2-1])
    elif option == 4:
        mass_solve()
    elif option == 5:
        optimize_problem()
    else:
        print("Invalid option")

    print()
    menu()
    option = int(input("Enter your option: "))

print("Goodbye!")
