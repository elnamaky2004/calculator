# Python Calculator – Matrices & Vectors

## Description
This is a console-based Python calculator that supports:  
- Basic arithmetic operations (add, subtract, multiply, divide, power, root, modulus).  
- 2x2 and 3x3 matrix operations (addition, subtraction, multiplication, determinant, transpose, inverse).  
- 2D and 3D vector operations (addition, subtraction, dot product, cross product, magnitude, normalization).  

The calculator allows the user to store up to 4 matrices or vectors per type (slots A, B, C, D) and perform multiple operations on them without losing data.

---

## Features
- Interactive menu system for easy navigation.  
- Slot-based storage for matrices and vectors.  
- Independent modes: user stays in the chosen mode until they explicitly choose to exit.  
- Input validation: prevents non-numeric inputs.  
- Cross product works for both 2D and 3D vectors.  
- Optional colored output if `colorama` is installed (or plain output without colors).

---

## Requirements
- Python 3.8 or higher  
- Optional for colored output: `colorama`
```bash
pip install colorama
Files
main.py – Main program with interactive menus.

operations.py – Basic arithmetic functions.

utils.py – Helper functions (e.g., get_num for numeric input).

matix.py – Matrix classes (Matrix2x2, Matrix3x3).

vectors.py – Vector class (Vector) with vector operations.

How to Run
Make sure all files are in the same directory.

Open terminal / command prompt in that directory.

Run the program:

bash
Copy code
python main.py
Follow the on-screen menu to choose operations.

Usage
Choose a mode:

Basic Calculator

Matrix 2x2

Matrix 3x3

Vectors

Exit

Inside each mode, follow prompts:

Create new matrices or vectors.

Perform operations on existing items in slots (A, B, C, D).

Stay in the mode until choosing Exit to return to the main menu.

Notes
Matrix inverse is only possible for non-singular matrices.

Cross product in 2D returns a scalar, in 3D returns a vector.

Input is validated to avoid crashes from non-numeric values.

Results are shown immediately, then program pauses so the user can view the output.

Author
Osama Elanamaky
