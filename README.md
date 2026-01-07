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
