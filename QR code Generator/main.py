import qrcode


def generate_QRcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="white")
    img.save("qrcode.png")


url = input("Enter a URL: ")
generate_QRcode(url)
