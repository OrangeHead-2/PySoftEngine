from math import tan, radians
from ..core.math3d import Vec3, Mat4

class Camera:
    def __init__(self, position, target, up, fov=60, aspect=1.0, near=0.1, far=1000):
        self.position = position
        self.target = target
        self.up = up
        self.fov = fov
        self.aspect = aspect
        self.near = near
        self.far = far

    def get_view_matrix(self):
        forward = self.target.subtract(self.position)
        # Normalize forward vector.
        f_len = (forward.dot(forward))**0.5
        forward = forward.scale(1 / f_len)
        right = forward.cross(self.up)
        r_len = (right.dot(right))**0.5
        right = right.scale(1 / r_len)
        up = right.cross(forward)
        mat = Mat4.identity()
        # Set rotation.
        mat.data[0][0] = right.x
        mat.data[0][1] = right.y
        mat.data[0][2] = right.z
        mat.data[1][0] = up.x
        mat.data[1][1] = up.y
        mat.data[1][2] = up.z
        mat.data[2][0] = -forward.x
        mat.data[2][1] = -forward.y
        mat.data[2][2] = -forward.z
        # Set translation.
        mat.data[0][3] = -right.dot(self.position)
        mat.data[1][3] = -up.dot(self.position)
        mat.data[2][3] = forward.dot(self.position)
        return mat

    def get_projection_matrix(self):
        fov_rad = radians(self.fov)
        f = 1 / tan(fov_rad / 2)
        a = self.aspect
        n = self.near
        f_dist = self.far
        mat = Mat4()
        mat.data[0][0] = f / a
        mat.data[1][1] = f
        mat.data[2][2] = (f_dist + n) / (n - f_dist)
        mat.data[2][3] = (2 * f_dist * n) / (n - f_dist)
        mat.data[3][2] = -1
        mat.data[3][3] = 0
        return mat