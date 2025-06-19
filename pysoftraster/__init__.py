# PySoftRaster - Minimal Software Rendering Library
# Import core modules
from .core.buffer import PixelBuffer
from .core.color import Color
from .core.math2d import Vec2
from .core.math3d import Vec3, Mat4
from .core.geometry import Geometry
from .core.rasterizer2d import Rasterizer2D
from .core.rasterizer3d import Rasterizer3D
from .core.depth_buffer import DepthBuffer
from .scene.camera import Camera
from .scene.mesh import Mesh
from .scene.obj_loader import ObjLoader
from .io.writer import FileWriter
from .io.viewport import Viewport

__all__ = [
    "PixelBuffer", "Color", "Vec2", "Vec3", "Mat4", "Geometry",
    "Rasterizer2D", "Rasterizer3D", "DepthBuffer", "Camera", "Mesh",
    "ObjLoader", "FileWriter", "Viewport"
]