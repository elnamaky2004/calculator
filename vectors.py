import math

class Vector:
    def __init__(self, x=0.0, y=0.0, z=None):
        self.x = x
        self.y = y
        self.z = 0.0 if z is None else z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        if self.z == 0 and other.z == 0:
            return self.x * other.y - self.y * other.x
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0, self.z)
        return Vector(self.x / mag, self.y / mag, self.z / mag)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

def test_vectors():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print("v1:", v1)
    print("v2:", v2)
    print("Addition:", v1 + v2)
    print("Subtraction:", v1 - v2)
    print("Dot Product:", v1.dot(v2))
    print("Cross Product (2D):", v1.cross(v2))
    print("Magnitude of v1:", v1.magnitude())
    print("Normalization of v1:", v1.normalize())
if __name__ == "__main__":
    test_vectors()    
