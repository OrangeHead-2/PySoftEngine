class FileWriter:
    @staticmethod
    def write_ppm(pixel_buffer, filename):
        pixel_buffer.export_ppm(filename)