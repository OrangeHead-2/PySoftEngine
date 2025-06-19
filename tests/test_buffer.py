from pysoftraster.core.buffer import PixelBuffer

def test_set_pixel():
    buffer = PixelBuffer(5, 5)
    buffer.set_pixel(2, 2, (123, 234, 56))
    assert buffer.buffer[2][2] == (123, 234, 56), "Pixel not set correctly."

def test_export_ppm(tmp_filename="test_output.ppm"):
    buffer = PixelBuffer(3, 3)
    # Set the center pixel to white.
    buffer.set_pixel(1, 1, (255, 255, 255))
    buffer.export_ppm(tmp_filename)
    # Read the file and check the header.
    with open(tmp_filename, "rb") as f:
        content = f.read()
    header = f"P6\n3 3\n255\n".encode()
    assert content.startswith(header), "PPM header is incorrect."

if __name__ == "__main__":
    test_set_pixel()
    test_export_ppm()
    print("test_buffer passed.")