from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib


path = Path("paquete_nativos/holamundo.png")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Hola mundo"
mensaje["to"] = "ultimatepython@holamundo.io"
mensaje["subject"] = "esto es una prueba"
cuerpo = MIMEText("Cuerpo del mensaje")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("ultimatepython@holamundo.io", "Hola mundo123")
    smtp.send_message(mensaje)
    print("Mensaje enviado!")
