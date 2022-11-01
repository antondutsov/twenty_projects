"""since we need python to create a image firs we will install the “Image” library and bc that image contains text which is need to be translate into a 2D machine code we will install “qr” library.
"""
# pip install qr Image - on Windows and Linux OS
# pip3 install qr Image - on MacOS

# Importing library
import qrcode


def generate_qrcode(text):
    # Data to encode
    text = "Python QR Generator"

    # Creating an instance of QRCode class
    qr = qrcode.QRCode(version=1,
                       box_size=10,
                       border=5)

    # Adding data to the instance 'qr'
    qr.add_data(text)

    qr.make(fit=True)
    img = qr.make_image(fill_color='green',
                        back_color='white')

    img.save('QR_image.png')


user_input = input("Enter your text to be converted into QR Code: ")

generate_qrcode(user_input)
