import math
from pysoftraster.core.buffer import PixelBuffer
from pysoftraster.core.color import Color
from pysoftraster.core.rasterizer3d import Rasterizer3D
from pysoftraster.scene.camera import Camera
from pysoftraster.scene.mesh import Mesh

# Reuse the transformation helper function.
def transform_point(mat, vec):
    x, y, z = vec.x, vec.y, vec.z
    w = 1.0
    x_prime = mat.data[0][0]*x + mat.data[0][1]*y + mat.data[0][2]*z + mat.data[0][3]*w
    y_prime = mat.data[1][0]*x + mat.data[1][1]*y + mat.data[1][2]*z + mat.data[1][3]*w
    z_prime = mat.data[2][0]*x + mat.data[2][1]*y + mat.data[2][2]*z + mat.data[2][3]*w
    w_prime = mat.data[3][0]*x + mat.data[3][1]*y + mat.data[3][2]*z + mat.data[3][3]*w
    if w_prime != 0:
        x_prime /= w_prime
        y_prime /= w_prime
        z_prime /= w_prime
    return (x_prime, y_prime, z_prime)

# Function to create a cube mesh with an adjustable horizontal offset.
def create_cube(offset):
    from pysoftraster.core.math3d import Vec3
    vertices = [
        Vec3(-1 + offset, -1,  1),
        Vec3( 1 + offset, -1,  1),
        Vec3( 1 + offset,  1,  1),
        Vec3(-1 + offset,  1,  1),
        Vec3(-1 + offset, -1, -1),
        Vec3( 1 + offset, -1, -1),
        Vec3( 1 + offset,  1, -1),
        Vec3(-1 + offset,  1, -1),
    ]
    faces = [
        (0, 1, 2), (0, 2, 3),
        (1, 5, 6), (1, 6, 2),
        (5, 4, 7), (5, 7, 6),
        (4, 0, 3), (4, 3, 7),
        (3, 2, 6), (3, 6, 7),
        (4, 5, 1), (4, 1, 0)
    ]
    return Mesh(vertices, faces)

def main():
    width, height = 800, 600
    buffer = PixelBuffer(width, height)
    
    from pysoftraster.core.math3d import Vec3, Mat4
    # Place the camera further to capture a wide scene.
    camera = Camera(position=Vec3(0, 0, -10), target=Vec3(0, 0, 0), up=Vec3(0, 1, 0), fov=90, aspect=width/height)
    rasterizer = Rasterizer3D(buffer, camera)
    rasterizer.clear((20, 20, 20))
    
    view = camera.get_view_matrix()
    proj = camera.get_projection_matrix()
    transform = proj.multiply(view)
    
    # Create two cubes with different horizontal offsets.
    cube1 = create_cube(-2)
    cube2 = create_cube(2)
    
    for cube in [cube1, cube2]:
        for face in cube.faces:
            points = []
            for idx in face:
                world_pt = cube.vertices[idx]
                x, y, z = transform_point(transform, world_pt)
                screen_x = int((x + 1) * 0.5 * width)
                screen_y = int((1 - (y + 1) * 0.5) * height)
                points.append((world_pt, screen_x, screen_y))
            # Use white for the left cube and red for the right cube.
            color = (255, 255, 255) if cube is cube1 else (255, 0, 0)
            rasterizer.draw_triangle(points[0], points[1], points[2], color)
    
    output_file = "scene_output.ppm"
    buffer.export_ppm(output_file)
    print(f"Scene rendered to {output_file}")

if __name__ == "__main__":
    main()