import qrcode

img = qrcode.make("https://www.youtube.com/@pythonschool-py")
img.save("channel_qr.png")
print("QR code generated successfully")
