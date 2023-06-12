# import struct



# # Open the image file in binary mode
# with open('nature2.jpg', 'rb') as f:

#     # Read the first 24 bytes of the image file
#     header = f.read(24)

#     # The width of the image is stored at bytes 16 and 17
#     width = struct.unpack('>H', header[16:18])[0]

#     # The height of the image is stored at bytes 18 and 19
#     height = struct.unpack('>H', header[18:20])[0]

#     # Display the size of the image
#     print("The image is {}x{}".format(width, height))

import struct



# Open the image file in binary mode
with open('nature2.jpg', 'rb') as f:

    # Read the first 24 bytes of the image file
    header = f.read(24)

    # The width of the image is stored at bytes 16 and 17
    width = struct.unpack('>H', header[16:18])[0]

    # The height of the image is stored at bytes 18 and 19
    height = struct.unpack('>H', header[18:20])[0]

    # Create a new PNG image
    png_image = open('nature2.png', 'wb')

    # Write the header to the PNG image
    png_image.write(b'\x89PNG\r\n\x1a\n')

    # Write the width and height of the image to the PNG image
    png_image.write(struct.pack('>i', width))
    png_image.write(struct.pack('>i', height))

    # Write the pixel data to the PNG image
    for y in range(height):
        for x in range(width):
            r, g, b = struct.unpack('>RGB', f.read(3))
            png_image.write(struct.pack('>RGB', r, g, b))

    # Close the PNG image
    png_image.close()

    # Create a new TIFF image
    tif_image = open('nature.tif', 'wb')

    # Write the header to the TIFF image
    tif_image.write(b'II')
    tif_image.write(struct.pack('>L', 42))
    tif_image.write(struct.pack('>L', 0))
    tif_image.write(struct.pack('>L', 0))
    tif_image.write(struct.pack('>L', width))
    tif_image.write(struct.pack('>L', height))
    tif_image.write(struct.pack('>L', 1))
    tif_image.write(struct.pack('>L', 8))
    tif_image.write(struct.pack('>L', 0))
    tif_image.write(struct.pack('>L', 0))
    tif_image.write(struct.pack('>L', 0))
    tif_image.write(struct.pack('>L', 0))

    # Write the pixel data to the TIFF image
    for y in range(height):
        for x in range(width):
            r, g, b = struct.unpack('>RGB', f.read(3))
            tif_image.write(struct.pack('>B', r))
            tif_image.write(struct.pack('>B', g))
            tif_image.write(struct.pack('>B', b))

    # Close the TIFF image
    tif_image.close()

    # Close the JPEG image
    f.close()

# import struct

# # Get the name of the JPEG image file from the command line
# image_file = sys.argv[1]

# # Open the image file in binary mode
# with open(image_file, 'rb') as f:

#     # Read the first 24 bytes of the image file
#     header = f.read(24)

#     # The width of the image is stored at bytes 16 and 17
#     width = struct.unpack('>H', header[16:18])[0]

#     # The height of the image is stored at bytes 18 and 19
#     height = struct.unpack('>H', header[18:20])[0]

#     # Create a new grayscale image
#     grayscale_image = open('grayscale_image.jpg', 'wb')

#     # Write the header to the grayscale image
#     grayscale_image.write(header)

#     # Write the width and height of the image to the grayscale image
#     grayscale_image.write(struct.pack('>i', width))
#     grayscale_image.write(struct.pack('>i', height))

#     # Write the pixel data to the grayscale image
#     for y in range(height):
#         for x in range(width):
#             r, g, b = struct.unpack('>RGB', f.read(3))
#             # Calculate the grayscale value
#             grayscale_value = (r * 0.299 + g * 0.587 + b * 0.114)
#             # Write the grayscale value to the grayscale image
#             grayscale_image.write(struct.pack('>B', grayscale_value))

#     # Close the grayscale image
#     grayscale_image.close()

#     # Close the JPEG image
#     f.close()