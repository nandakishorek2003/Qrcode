import qrcode
url=input("enter URL:")
path="C:\\Users\\Sanjay G\\Desktop\\qrcode.png"
qr=qrcode.QRCode()
qr.add_data(url)
img=qr.make_image()
img.save(path)
print("qr code generated")