from src import put
import qrcode

# Generates a qr code
def qr():
    qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data("https://yildizskylab.com")
    qr.make()
    qr = qr.make_image().convert('RGB')
    return qr


"""
# Generates the certificate
def certificate(img):
    put.name()
    put.instructor()
    put.content()
    put.qr(qr)
"""
