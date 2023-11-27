# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# from string import Template
# import smtplib

# plantilla = Path("paquetes_nativos/plantilla.html").read_text("utf-8")
# template = Template(plantilla)
# # cuerpo = template.substitute({"usuario": "puerquito feliz"})
# cuerpo = template.substitute(usuario="puerquito feliz")


# path = Path("paquete_nativos/holamundo.png")
# mime_image = MIMEImage(path.read_bytes())
# mensaje = MIMEMultipart()
# mensaje["from"] = "Hola mundo"
# mensaje["to"] = "ultimatepython@holamundo.io"
# mensaje["subject"] = "esto es una prueba"
# cuerpo = MIMEText(cuerpo, "html")
# mensaje.attach(cuerpo)
# mensaje.attach(mime_image)

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()

#     smtp.login("ultimatepython@holamundo.io", "Hola mundo123")
#     smtp.send_message(mensaje)
#     print("Mensaje enviado!")


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

plantilla = Path("paquetes_nativos/plantilla.html").read_text("utf-8")
template = Template(plantilla)
cuerpo = template.substitute(usuario="puerquito feliz")

path_imagen = Path("paquete_nativos/holamundo.png")
mime_image = MIMEImage(path_imagen.read_bytes())
mime_image.add_header('Content-Disposition', 'attachment',
                      filename='holamundo.png')

mensaje = MIMEMultipart()
mensaje["from"] = "Hola mundo"
# Cambia la dirección de destino
mensaje["to"] = "danigarcia.negocio@gmail.com"
mensaje["subject"] = "Esto es una prueba"
cuerpo = MIMEText(cuerpo, "html")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

# Configuración para enviar correo desde Gmail
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    # Reemplaza con tu dirección de correo y contraseña o la contraseña de aplicación generada
    smtp.login("tu_correo@gmail.com", "tu_contraseña")

    smtp.send_message(mensaje)
    print("Mensaje enviado!")
