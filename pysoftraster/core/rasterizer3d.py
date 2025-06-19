from .depth_buffer import DepthBuffer

class Rasterizer3D:
    def __init__(self, pixel_buffer, camera):
        self.pixel_buffer = pixel_buffer
        self.camera = camera
        self.depth_buffer = DepthBuffer(pixel_buffer.width, pixel_buffer.height)

    def clear(self, color=(0, 0, 0)):
        for y in range(self.pixel_buffer.height):
            for x in range(self.pixel_buffer.width):
                self.pixel_buffer.set_pixel(x, y, color)
        self.depth_buffer.clear()

    def draw_triangle(self, p0, p1, p2, color):
        # p0, p1, p2 are tuples: (world_pos(Vec3), screen_x, screen_y)
        x0, y0 = p0[1], p0[2]
        x1, y1 = p1[1], p1[2]
        x2, y2 = p2[1], p2[2]
        # Bounding box (clamped to screen)
        min_x = max(min(x0, x1, x2), 0)
        max_x = min(max(x0, x1, x2), self.pixel_buffer.width - 1)
        min_y = max(min(y0, y1, y2), 0)
        max_y = min(max(y0, y1, y2), self.pixel_buffer.height - 1)

        area = self.edge_function(x0, y0, x1, y1, x2, y2)
        if area == 0:
            return

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                w0 = self.edge_function(x1, y1, x2, y2, x, y)
                w1 = self.edge_function(x2, y2, x0, y0, x, y)
                w2 = self.edge_function(x0, y0, x1, y1, x, y)
                if w0 >= 0 and w1 >= 0 and w2 >= 0:
                    w0 /= area
                    w1 /= area
                    w2 /= area
                    # Interpolate z-depth from the world positions.
                    z = p0[0].z * w0 + p1[0].z * w1 + p2[0].z * w2
                    if z < self.depth_buffer.get(x, y):
                        self.depth_buffer.set(x, y, z)
                        self.pixel_buffer.set_pixel(x, y, color)

    def edge_function(self, x0, y0, x1, y1, x, y):
        return (x - x0) * (y1 - y0) - (y - y0) * (x1 - x0)