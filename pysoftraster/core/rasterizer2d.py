from .geometry import Geometry

class Rasterizer2D:
    def __init__(self, pixel_buffer):
        self.pixel_buffer = pixel_buffer

    def draw_line(self, x0, y0, x1, y1, color):
        points = Geometry.line_bresenham(x0, y0, x1, y1)
        for x, y in points:
            self.pixel_buffer.set_pixel(x, y, color)

    def fill_polygon(self, vertices, color):
        # Simple scanline fill algorithm; vertices is a list of (x, y) tuples.
        xs = [v[0] for v in vertices]
        ys = [v[1] for v in vertices]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        for y in range(min_y, max_y + 1):
            intersections = []
            n = len(vertices)
            for i in range(n):
                x1, y1 = vertices[i]
                x2, y2 = vertices[(i + 1) % n]
                if y1 == y2:
                    continue
                if y < min(y1, y2) or y > max(y1, y2):
                    continue
                # Linear interpolation for x-intersection.
                x_int = int(x1 + (y - y1) * (x2 - x1) / (y2 - y1))
                intersections.append(x_int)
            intersections.sort()
            for i in range(0, len(intersections), 2):
                if i + 1 < len(intersections):
                    for x in range(intersections[i], intersections[i + 1] + 1):
                        self.pixel_buffer.set_pixel(x, y, color)