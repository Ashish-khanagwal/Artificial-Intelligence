import qrcode

data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename (with .png extension at the end): ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
img = qr.make_image(fill_color="black", back_color="white")
img.save(filename)
print(f"QR code saved as {filename}")
