from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        # text/plain = MIME-тип
        # TODO: Прочитать статью https://ru.wikipedia.org/wiki/Список_MIME-типов
        # и отметить основные майм-типы, которые может отправлять сервер клиенту.
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        my_datetime = datetime.now().strftime('%d.%m.%y %H:%M:%S')
        result = f"Александр Волжанин, {my_datetime}"
        self.wfile.write(bytes(result, "utf-8"))


httpd = HTTPServer(('127.0.0.1', 8080), SimpleHTTPRequestHandler)
print('server is running ')
httpd.serve_forever()