import math

ASCII_CHARS = "@%#*+=-:. "

class AsciiRenderer:
    def __init__(self, width, height, shades=ASCII_CHARS):
        self.width = width
        self.height = height
        self.shades = shades

    def render(self, zbuffer, colorbuffer):
        # zbuffer: 2D depth array
        # colorbuffer: 2D gray (0..255) or tuple
        out = []
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                c = colorbuffer[y][x]
                if isinstance(c, tuple):
                    g = int(0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2])
                else:
                    g = int(c)
                idx = int((g/255) * (len(self.shades)-1))
                line += self.shades[idx]
            out.append(line)
        return "\n".join(out)

    def show(self, zbuffer, colorbuffer):
        print(self.render(zbuffer, colorbuffer))