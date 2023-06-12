with open("project source code.jpg", "rb") as f:
    jpeg_data = f.read()
png_header = b"\x89PNG\r\n\x1a\n"
png_data = png_header + jpeg_data
with open("cat.png", "wb") as f:
    f.write(png_data)
tif_header = b"II*\x00\x08\x00\x00\x00"
tif_data = tif_header + jpeg_data
with open("cat.tif", "wb") as f:
    f.write(tif_data)

