from ..core.math3d import Vec3
from .mesh import Mesh

class ObjLoader:
    @staticmethod
    def load(filename):
        vertices = []
        faces = []
        with open(filename, "r") as file:
            for line in file:
                if line.startswith("v "):
                    parts = line.split()
                    x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                    vertices.append(Vec3(x, y, z))
                elif line.startswith("f "):
                    parts = line.split()
                    # Faces in OBJ files are 1-indexed.
                    face = [int(part.split("/")[0]) - 1 for part in parts[1:]]
                    faces.append(tuple(face))
        return Mesh(vertices, faces)