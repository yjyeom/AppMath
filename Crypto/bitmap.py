import struct
from PIL import Image
import os
from Crypto.Cipher import AES

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


def load_and_convert_to_grayscale(image_path, output_path):
    """
    Load an image file and convert it to grayscale bitmap file.

    Args:
        image_path: Path to input image file
        output_path: Path to output grayscale BMP file
    """
    
    # Load image and convert to grayscale
    img = Image.open(image_path).convert('L')
    
    # Get dimensions
    width, height = img.size
    
    # Flip image vertically
    img = img.transpose(Image.FLIP_TOP_BOTTOM)

    # Convert image data to bytes
    data = list(img.getdata())
    
    # Create grayscale bitmap
    create_grayscale_bitmap(width, height, data, output_path)


def encrypt_data_aes_ecb(data, key, filename):
    """
    Encrypt byte array using AES ECB mode.
    
    Args:
        data: Byte array to encrypt
        key: Encryption key (16, 24, or 32 bytes)
        filename: Output encrypted file path
    """
    
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Pad data to multiple of 16 bytes
    padding_length = 16 - (len(data) % 16)
    padded_data = data + bytes([padding_length] * padding_length)
    
    encrypted_data = cipher.encrypt(padded_data)
    
    with open(filename, 'wb') as f:
        f.write(encrypted_data)


def encrypt_data_aes_cbc(data, key, iv, filename):
    """
    Encrypt byte array using AES CBC mode.
    
    Args:
        data: Byte array to encrypt
        key: Encryption key (16, 24, or 32 bytes)
        iv: Initialization vector (16 bytes)
        filename: Output encrypted file path
    """
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad data to multiple of 16 bytes
    padding_length = 16 - (len(data) % 16)
    padded_data = data + bytes([padding_length] * padding_length)
    
    encrypted_data = cipher.encrypt(padded_data)
    
    with open(filename, 'wb') as f:
        f.write(encrypted_data)        

# Load grayscale BMP and convert to data array
def load_grayscale_bitmap(filename):
    """
    Load a grayscale BMP file and extract data as array.
    
    Args:
        filename: Path to grayscale BMP file
        
    Returns:
        Tuple of (width, height, data_array)
    """
    img = Image.open(filename).convert('L')
    width, height = img.size
    data = list(img.getdata())
    return width, height, data

# Example usage
if __name__ == '__main__':

    os.chdir('d:/salt_data/Salt_Git_2026/AppMath/Crypto')  

    width, height = 32, 32
    data = [i % 2 for i in range(width * height)]
    create_bitmap(width, height, data, 'output.bmp')   
    print("Bitmap created successfully as 'output.bmp'")

    # Create a grayscale bitmap
    grayscale_data = [i % 256 for i in range(width * height)]
    create_grayscale_bitmap(width, height, grayscale_data, 'grayscale_output.bmp')
    print("Grayscale bitmap created successfully as 'grayscale_output.bmp'")

    # Load an image and convert to grayscale bitmap
    load_and_convert_to_grayscale('KMU-logo.bmp', 'KMU-grayscale.bmp')

    # Load the grayscale BMP file
    width, height, data = load_grayscale_bitmap('KMU-grayscale.bmp')
    print(f"Loaded image: {width}x{height}, data length: {len(data)}")
    #print(f"First 10 pixels: {data[:10]}")

    encrypt_data_aes_ecb(bytes(data), b'secretkey1234500', 'e-KMU-grayscale.bin')
    encrypt_data_aes_cbc(bytes(data), b'secretkey1234500', b'iv12345678901234', 'e-KMU-grayscale-cbc.bin')
    
    # Read encrypted file as byte array
    with open('e-KMU-grayscale.bin', 'rb') as f:
        encrypted_data = f.read()
    print(f"Encrypted data length: {len(encrypted_data)}")
    width, height = 384, 134
    create_grayscale_bitmap(width, height, encrypted_data[:width*height], 'e-KMU-grayscale.bmp')

    with open('e-KMU-grayscale-cbc.bin', 'rb') as f:
        encrypted_data = f.read()
    print(f"Encrypted data length: {len(encrypted_data)}")
    width, height = 384, 134
    create_grayscale_bitmap(width, height, encrypted_data[:width*height], 'e-KMU-grayscale-cbc.bmp')


