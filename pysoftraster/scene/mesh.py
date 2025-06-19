class Mesh:
    def __init__(self, vertices=None, faces=None):
        # vertices: list of Vec3 objects.
        # faces: list of tuples (indices into vertices list).
        self.vertices = vertices if vertices else []
        self.faces = faces if faces else []