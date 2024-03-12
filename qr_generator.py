import qrcode

def generate_qr_code(link, output_filename):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(output_filename)

if __name__ == "__main__":
    # Example usage
    link_to_encode = "https://dsmru.up.nic.in/"
    output_file = "example_qr_code.png"

    generate_qr_code(link_to_encode, output_file)
    print(f"QR code generated and saved as {output_file}")
