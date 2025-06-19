from pysoftraster.core.buffer import PixelBuffer
from pysoftraster.core.rasterizer2d import Rasterizer2D
from pysoftraster.core.color import Color
from pysoftraster.core.geometry import Geometry

def test_draw_line():
    width, height = 10, 10
    buffer = PixelBuffer(width, height)
    rasterizer = Rasterizer2D(buffer)
    white = (255, 255, 255)
    rasterizer.draw_line(0, 0, 9, 9, white)
    
    # Bresenham's line from (0,0) to (9,9) should produce a number of points matching the algorithm.
    line_points = Geometry.line_bresenham(0, 0, 9, 9)
    count = 0
    for y in range(height):
        for x in range(width):
            if buffer.buffer[y][x] == white:
                count += 1
    assert count == len(line_points), f"Expected {len(line_points)} points, got {count}"

if __name__ == "__main__":
    test_draw_line()
    print("test_rasterizer2d passed.")