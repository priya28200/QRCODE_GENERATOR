import qrcode

def generate_qr_code(url, save_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=5,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)
url_to_encode = "https://qrcodecreator.com"
output_path = "qrcodecreator_qr_code.png"
generate_qr_code(url_to_encode, output_path)
