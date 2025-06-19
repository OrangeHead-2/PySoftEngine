class PixelBuffer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.buffer = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.buffer[y][x] = color

    def export_ppm(self, filename):
        with open(filename, "wb") as f:
            header = f"P6\n{self.width} {self.height}\n255\n"
            f.write(header.encode())
            for row in self.buffer:
                for r, g, b in row:
                    f.write(bytes((r, g, b)))