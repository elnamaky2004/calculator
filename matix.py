class Matrix2x2:
    def __init__(self, a11, a12, a21, a22):
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22

    def __add__(self, other):
        return Matrix2x2(
            self.a11 + other.a11,
            self.a12 + other.a12,
            self.a21 + other.a21,
            self.a22 + other.a22
        )

    def __sub__(self, other):
        return Matrix2x2(
            self.a11 - other.a11,
            self.a12 - other.a12,
            self.a21 - other.a21,
            self.a22 - other.a22
        )

    def __mul__(self, other):
        if isinstance(other, Matrix2x2):
            return Matrix2x2(
                self.a11 * other.a11 + self.a12 * other.a21,
                self.a11 * other.a12 + self.a12 * other.a22,
                self.a21 * other.a11 + self.a22 * other.a21,
                self.a21 * other.a12 + self.a22 * other.a22
            )
        return Matrix2x2(
            self.a11 * other,
            self.a12 * other,
            self.a21 * other,
            self.a22 * other
        )

    def determinant(self):
        return self.a11 * self.a22 - self.a12 * self.a21

    def transpose(self):
        return Matrix2x2(
            self.a11, self.a21,
            self.a12, self.a22
        )

    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Singular matrix")
        return Matrix2x2(
            self.a22 / det,
            -self.a12 / det,
            -self.a21 / det,
            self.a11 / det
        )

    def __str__(self):
        return f"[{self.a11} {self.a12}]\n[{self.a21} {self.a22}]"
class Matrix3x3:
    def __init__(self, a11, a12, a13, a21, a22, a23, a31, a32, a33):
        self.a11, self.a12, self.a13 = a11, a12, a13
        self.a21, self.a22, self.a23 = a21, a22, a23
        self.a31, self.a32, self.a33 = a31, a32, a33

    def __add__(self, other):
        return Matrix3x3(
            self.a11 + other.a11, self.a12 + other.a12, self.a13 + other.a13,
            self.a21 + other.a21, self.a22 + other.a22, self.a23 + other.a23,
            self.a31 + other.a31, self.a32 + other.a32, self.a33 + other.a33
        )

    def __sub__(self, other):
        return Matrix3x3(
            self.a11 - other.a11, self.a12 - other.a12, self.a13 - other.a13,
            self.a21 - other.a21, self.a22 - other.a22, self.a23 - other.a23,
            self.a31 - other.a31, self.a32 - other.a32, self.a33 - other.a33
        )

    def __mul__(self, other):
        if isinstance(other, Matrix3x3):
            return Matrix3x3(
                self.a11*other.a11 + self.a12*other.a21 + self.a13*other.a31,
                self.a11*other.a12 + self.a12*other.a22 + self.a13*other.a32,
                self.a11*other.a13 + self.a12*other.a23 + self.a13*other.a33,

                self.a21*other.a11 + self.a22*other.a21 + self.a23*other.a31,
                self.a21*other.a12 + self.a22*other.a22 + self.a23*other.a32,
                self.a21*other.a13 + self.a22*other.a23 + self.a23*other.a33,

                self.a31*other.a11 + self.a32*other.a21 + self.a33*other.a31,
                self.a31*other.a12 + self.a32*other.a22 + self.a33*other.a32,
                self.a31*other.a13 + self.a32*other.a23 + self.a33*other.a33
            )
        return Matrix3x3(
            self.a11*other, self.a12*other, self.a13*other,
            self.a21*other, self.a22*other, self.a23*other,
            self.a31*other, self.a32*other, self.a33*other
        )

    def determinant(self):
        return (
            self.a11*(self.a22*self.a33 - self.a23*self.a32)
            - self.a12*(self.a21*self.a33 - self.a23*self.a31)
            + self.a13*(self.a21*self.a32 - self.a22*self.a31)
        )

    def transpose(self):
        return Matrix3x3(
            self.a11, self.a21, self.a31,
            self.a12, self.a22, self.a32,
            self.a13, self.a23, self.a33
        )

    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Singular matrix")
        return Matrix3x3(
            (self.a22*self.a33 - self.a23*self.a32)/det,
            (self.a13*self.a32 - self.a12*self.a33)/det,
            (self.a12*self.a23 - self.a13*self.a22)/det,

            (self.a23*self.a31 - self.a21*self.a33)/det,
            (self.a11*self.a33 - self.a13*self.a31)/det,
            (self.a13*self.a21 - self.a11*self.a23)/det,

            (self.a21*self.a32 - self.a22*self.a31)/det,
            (self.a12*self.a31 - self.a11*self.a32)/det,
            (self.a11*self.a22 - self.a12*self.a21)/det
        )

    def __str__(self):
        return (
            f"[{self.a11} {self.a12} {self.a13}]\n"
            f"[{self.a21} {self.a22} {self.a23}]\n"
            f"[{self.a31} {self.a32} {self.a33}]"
        )
def test_matrix2x2():
    A = Matrix2x2(1, 2, 3, 4)
    B = Matrix2x2(5, 6, 7, 8)

    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)

    print("\nA + B:")
    print(A + B)

    print("\nA - B:")
    print(A - B)

    print("\nA * B:")
    print(A * B)

    print("\nDeterminant of A:")
    print(A.determinant())

    print("\nTranspose of A:")
    print(A.transpose())

    print("\nInverse of A:")
    print(A.inverse())
def test_matrix3x3():
    A = Matrix3x3(1, 2, 3, 0, 1, 4, 5, 6, 0)
    B = Matrix3x3(7, 8, 9, 1, 0, 2, 3, 4, 5)

    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)

    print("\nA + B:")
    print(A + B)

    print("\nA - B:")
    print(A - B)

    print("\nA * B:")
    print(A * B)

    print("\nDeterminant of A:")
    print(A.determinant())

    print("\nTranspose of A:")
    print(A.transpose())

    print("\nInverse of A:")
    print(A.inverse())
if __name__ == "__main__":
    print("Testing 2x2 Matrix Operations:")
    test_matrix2x2()
    print("\nTesting 3x3 Matrix Operations:")
    test_matrix3x3()        