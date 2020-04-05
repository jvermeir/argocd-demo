from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime

PORT = 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        x = datetime.datetime.now()

        self.wfile.write(str.encode(str(x)))


httpd = HTTPServer(('0.0.0.0', PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()