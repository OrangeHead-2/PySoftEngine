class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def subtract(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def scale(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )


class Mat4:
    def __init__(self):
        self.data = [[0.0 for _ in range(4)] for _ in range(4)]

    @staticmethod
    def identity():
        mat = Mat4()
        for i in range(4):
            mat.data[i][i] = 1.0
        return mat

    def multiply(self, other):
        result = Mat4()
        for i in range(4):
            for j in range(4):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(4))
        return result