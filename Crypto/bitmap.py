import struct

def create_bitmap(width, height, data, filename):
    """
    Create a black and white bitmap file from binary data.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        data: List or bytes of binary values (0 or 1)
        filename: Output bitmap file path
    """
    # BMP header
    file_size = 54 + (width * height // 8)
    
    bmp_header = b'BM'
    bmp_header += struct.pack('<I', file_size)  # File size
    bmp_header += struct.pack('<I', 0)  # Reserved
    bmp_header += struct.pack('<I', 54)  # Data offset
    
    # DIB header
    dib_header = struct.pack('<I', 40)  # Header size
    dib_header += struct.pack('<i', width)  # Width
    dib_header += struct.pack('<i', height)  # Height
    dib_header += struct.pack('<H', 1)  # Planes
    dib_header += struct.pack('<H', 1)  # Bits per pixel
    dib_header += struct.pack('<I', 0)  # Compression
    dib_header += struct.pack('<I', 0)  # Image size
    dib_header += struct.pack('<i', 0)  # X pixels per meter
    dib_header += struct.pack('<i', 0)  # Y pixels per meter
    dib_header += struct.pack('<I', 0)  # Colors used
    dib_header += struct.pack('<I', 0)  # Important colors
    
    # Color palette (black and white)
    palette = b'\x00\x00\x00\x00'  # Black
    palette += b'\xff\xff\xff\x00'  # White
    
    # Bitmap data
    bitmap_data = b''
    for y in range(height):
        row = b''
        for x in range(0, width, 8):
            byte = 0
            for bit in range(8):
                if x + bit < width and data[y * width + x + bit]:
                    byte |= (0x80 >> bit)
            row += bytes([byte])
        bitmap_data += row
    
    # Write file
    with open(filename, 'wb') as f:
        f.write(bmp_header + dib_header + palette + bitmap_data)


def create_grayscale_bitmap(width, height, data, filename):
    """
    Create a grayscale bitmap file from byte array data.

    Args:
        width: Image width in pixels
        height: Image height in pixels
        data: List or bytes of grayscale values (0-255)
        filename: Output bitmap file path
    """
    # BMP header
    file_size = 54 + 1024 + (width * height)

    bmp_header = b'BM'
    bmp_header += struct.pack('<I', file_size)
    bmp_header += struct.pack('<I', 0)
    bmp_header += struct.pack('<I', 1078)  # Data offset (54 + 1024)

    # DIB header
    dib_header = struct.pack('<I', 40)
    dib_header += struct.pack('<i', width)
    dib_header += struct.pack('<i', height)
    dib_header += struct.pack('<H', 1)
    dib_header += struct.pack('<H', 8)  # 8 bits per pixel
    dib_header += struct.pack('<I', 0)
    dib_header += struct.pack('<I', 0)
    dib_header += struct.pack('<i', 0)
    dib_header += struct.pack('<i', 0)
    dib_header += struct.pack('<I', 256)  # Colors used
    dib_header += struct.pack('<I', 0)

    # Grayscale palette (0-255)
    palette = b''
    for i in range(256):
        palette += bytes([i, i, i, 0])

    # Bitmap data
    bitmap_data = bytes(data)

    # Write file
    with open(filename, 'wb') as f:
        f.write(bmp_header + dib_header + palette + bitmap_data)

# Example usage
if __name__ == '__main__':
    width, height = 32, 32
    data = [i % 2 for i in range(width * height)]
    create_bitmap(width, height, data, 'output.bmp')   
    print("Bitmap created successfully as 'output.bmp'")

    # Create a grayscale bitmap
    grayscale_data = [i % 256 for i in range(width * height)]
    create_grayscale_bitmap(width, height, grayscale_data, 'grayscale_output.bmp')
    print("Grayscale bitmap created successfully as 'grayscale_output.bmp'")