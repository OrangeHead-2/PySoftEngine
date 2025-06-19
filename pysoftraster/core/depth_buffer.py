class DepthBuffer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.buffer = [[float("inf") for _ in range(width)] for _ in range(height)]

    def clear(self):
        self.buffer = [[float("inf") for _ in range(self.width)] for _ in range(self.height)]

    def get(self, x, y):
        return self.buffer[y][x]

    def set(self, x, y, value):
        self.buffer[y][x] = value