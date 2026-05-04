import qrcode

# URL
data = "https://horario-quebrada.netlify.app/?utm_source=qr-code"

# Genera la instancia del código QR
qr = qrcode.QRCode(
  version=1,
  error_correction=qrcode.constants.ERROR_CORRECT_L,
  box_size=10,
  border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Imagen del código QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardar imagen del código QR
img.save("qr_transporte_quebrada.png")