class matrix2x2:
    def __init__(self, a11, a12, a21, a22):
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22

    def __add__(self, other):
        return matrix2x2(
            self.a11 + other.a11,
            self.a12 + other.a12,
            self.a21 + other.a21,
            self.a22 + other.a22
        )

    def __sub__(self, other):
        return matrix2x2(
            self.a11 - other.a11,
            self.a12 - other.a12,
            self.a21 - other.a21,
            self.a22 - other.a22
        )

    def __mul__(self, other):
        return matrix2x2(
            self.a11 * other.a11 + self.a12 * other.a21,
            self.a11 * other.a12 + self.a12 * other.a22,
            self.a21 * other.a11 + self.a22 * other.a21,
            self.a21 * other.a12 + self.a22 * other.a22
        )

    def determinant(self):
        return self.a11 * self.a22 - self.a12 * self.a21

    def transpose(self):
        return matrix2x2(
            self.a11,
            self.a21,
            self.a12,
            self.a22
        )
    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        return matrix2x2(
            self.a22 / det,
            -self.a12 / det,
            -self.a21 / det,
            self.a11 / det
        )

    def __repr__(self):
        return f"matrix2x2({self.a11}, {self.a12}, {self.a21}, {self.a22})"
class matrix3x3:
    def __init__(self, a11, a12, a13, a21, a22, a23, a31, a32, a33):
        self.a11 = a11
        self.a12 = a12
        self.a13 = a13
        self.a21 = a21
        self.a22 = a22
        self.a23 = a23
        self.a31 = a31
        self.a32 = a32
        self.a33 = a33
    def __add__(self, other):
        return matrix3x3(
            self.a11 + other.a11,
            self.a12 + other.a12,
            self.a13 + other.a13,
            self.a21 + other.a21,
            self.a22 + other.a22,
            self.a23 + other.a23,
            self.a31 + other.a31,
            self.a32 + other.a32,
            self.a33 + other.a33
        )
    def __sub__(self, other):
        return matrix3x3(
            self.a11 - other.a11,
            self.a12 - other.a12,
            self.a13 - other.a13,
            self.a21 - other.a21,
            self.a22 - other.a22,
            self.a23 - other.a23,
            self.a31 - other.a31,
            self.a32 - other.a32,
            self.a33 - other.a33
        )
    def __mul__(self, other):
        return matrix3x3(
            self.a11 * other.a11 + self.a12 * other.a21 + self.a13 * other.a31,
            self.a11 * other.a12 + self.a12 * other.a22 + self.a13 * other.a32,
            self.a11 * other.a13 + self.a12 * other.a23 + self.a13 * other.a33,
            self.a21 * other.a11 + self.a22 * other.a21 + self.a23 * other.a31,
            self.a21 * other.a12 + self.a22 * other.a22 + self.a23 * other.a32,
            self.a21 * other.a13 + self.a22 * other.a23 + self.a23 * other.a33,
            self.a31 * other.a11 + self.a32 * other.a21 + self.a33 * other.a31,
            self.a31 * other.a12 + self.a32 * other.a22 + self.a33 * other.a32,
            self.a31 * other.a13 + self.a32 * other.a23 + self.a33 * other.a33
        )
    def determinant(self):
        return (self.a11 * (self.a22 * self.a33 - self.a23 * self.a32) -
                self.a12 * (self.a21 * self.a33 - self.a23 * self.a31) +
                self.a13 * (self.a21 * self.a32 - self.a22 * self.a31))
    def transpose(self):
        return matrix3x3(
            self.a11,
            self.a21,
            self.a31,
            self.a12,
            self.a22,
            self.a32,
            self.a13,
            self.a23,
            self.a33
        )
    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        return matrix3x3(
            (self.a22 * self.a33 - self.a23 * self.a32) / det,
            (self.a13 * self.a32 - self.a12 * self.a33) / det,
            (self.a12 * self.a23 - self.a13 * self.a22) / det,
            (self.a23 * self.a31 - self.a21 * self.a33) / det,
            (self.a11 * self.a33 - self.a13 * self.a31) / det,
            (self.a13 * self.a21 - self.a11 * self.a23) / det,
            (self.a21 * self.a32 - self.a22 * self.a31) / det,
            (self.a12 * self.a31 - self.a11 * self.a32) / det,
            (self.a11 * self.a22 - self.a12 * self.a21) / det
        )
    def __repr__(self):
        return (f"[{self.a11} {self.a12} {self.a13}]\n"
                f"[{self.a21} {self.a22} {self.a23}]\n"
                f"[{self.a31} {self.a32} {self.a33}]")        
def test_matrices():
    m1 = matrix2x2(1, 2, 3, 4)
    m2 = matrix2x2(5, 6, 7, 8)
    print("Matrix 2x2 Addition:\n", m1 + m2)
    print("Matrix 2x2 Subtraction:\n", m1 - m2)
    print("Matrix 2x2 Multiplication:\n", m1 * m2)
    print("Matrix 2x2 Determinant of m1:", m1.determinant())
    print("Matrix 2x2 Transpose of m1:\n", m1.transpose())
    print("Matrix 2x2 Inverse of m1:\n", m1.inverse())

    m3 = matrix3x3(1, 2, 3, 4, 5, 6, 7, 8, 9)
    m4 = matrix3x3(9, 8, 7, 6, 5, 4, 3, 2, 1)
    print("Matrix 3x3 Addition:\n", m3 + m4)
    print("Matrix 3x3 Subtraction:\n", m3 - m4)
    print("Matrix 3x3 Multiplication:\n", m3 * m4)
    print("Matrix 3x3 Determinant of m3:", m3.determinant())
    print("Matrix 3x3 Transpose of m3:\n", m3.transpose())
    try:
        print("Matrix 3x3 Inverse of m3:\n", m3.inverse())
    except ValueError as e:
        print(e)    
if __name__ == "__main__":
    test_matrices()        