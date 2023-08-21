from http.server import BaseHTTPRequestHandler, HTTPServer
import smtplib
import traceback

RESPONSE_STYLES = '''
<style>
    body {
        background-color: black;
        color: #00ff00; 
        font-family: monospace;
        text-align: center;
        padding-top: 50px;
    }

    h1 {
        font-size: 24px;
    }

    p {
        font-size: 18px;
        margin-top: 20px;
    }

    .button {
        padding: 10px 20px;
        font-size: 18px;
        background-color: #00ff00; 
        color: black;
        border: 2px solid black;
        border-radius: 5px;
        cursor: pointer;
        animation: falling-letters 2s forwards;
        text-decoration: none;
        display: inline-block;
        margin-top: 30px;
    }

    .button:hover {
        background-color: black;
        color: #00ff00;
    }
</style>
'''

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open("index.html", "r", encoding="utf-8") as f:
                response = f.read()
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def do_POST(self):
        if self.path == '/send-email':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            try:
                smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
                smtp_server.starttls()
                smtp_server.login('serviciosEscolaresUptx0@gmail.com', 'xyyaqkhwfxbmrlih')  # Reemplaza con tu dirección de correo y contraseña
                
                msg = "Subject: Capacitación Docente.\n\n"\
                      "Estimados/as docentes de la Universidad Politécnica de Tlaxcala.\n\n"\
                      "Espero que este mensaje los encuentre bien. Como parte del equipo de Servicios Escolares, "\
                      "me dirijo a ustedes con el más alto grado de consideración y respeto para informarles que han sido seleccionados para participar en una capacitación docente virtual, "\
                      "programada para llevarse a cabo el 20 de Agosto del presente año.\n\n"\
                      "Les solicitamos amablemente que se registren para esta importante capacitación accediendo al siguiente enlace: http://127.0.0.1:8080\n\n"\
                      "El propósito de esta capacitación es brindarles una actualización en las normativas educativas que serán implementadas en el próximo ciclo escolar, así como presentar las nuevas y efectivas metodologías de enseñanza que se aplicarán en nuestras aulas.\n\n"\
                      "La participación de cada uno/a de ustedes es de suma importancia, y su asistencia será de gran valor para el enriquecimiento de la experiencia educativa de nuestros estudiantes.\n\n"\
                      "Sin duda alguna, su compromiso y dedicación como docentes contribuirán significativamente al continuo progreso de nuestra institución.\n\n"\
                      "Les deseamos un excelente inicio de semana, y confiamos en contar con su grata presencia en este evento formativo y enriquecedor.\n\n"\
                      "Agradecemos de antemano su amable disposición y colaboración en esta noble tarea de fomentar el conocimiento y el crecimiento académico en nuestra comunidad educativa.\n\n"\
                      "Atentamente:\n"\
                      "Lic. María del R. Orea Galicia\n"\
                      "Teléfono de contacto: 2461200862\n"\
                      "Correo electrónico de contacto: mariaorea@uptx.edu.mx"
                msg = msg.encode('utf-8')  # Codificar el mensaje en UTF-8
                
                to_emails = ['renmieseas@gmail.com', 'anon.59re@gmail.com','Karenrodriguezzecua@gmail.com',
                             'alanhernandez2829@gmail.com', 'Karenitzel11@hotmail.com',
                             'urielngulo@gmail.com','ivanojedareyes777@gmail.com']
                smtp_server.sendmail('serviciosEscolaresUptx0@gmail.com', to_emails, msg)
                smtp_server.quit()
                
                response = "Correo enviado exitosamente."
            except Exception as e:
                error_msg = f"Error al enviar el correo:\n{traceback.format_exc()}"
                response = error_msg

            self.wfile.write(RESPONSE_STYLES.encode('utf-8'))
            self.wfile.write("<h1>Emails Masivos de Manera Automatizada.</h1>".encode('utf-8'))
            self.wfile.write(f"<p>{response}</p>".encode('utf-8'))
            self.wfile.write('<a class="button" href="/">Volver al inicio</a>'.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

def run(server_class=HTTPServer, handler_class=MyHandler, host='127.10.1.0', port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor escuchando en {host}:{port}...")
    httpd.serve_forever()

if __name__=='__main__':
    run()
