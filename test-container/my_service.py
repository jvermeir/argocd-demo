from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime

PORT = 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        text = str(datetime.datetime.now())
        print ("text: " + text)
        with open('git-hash.txt') as reader:
            version = reader.read()
            print ("new version: " + version)
        text = "new! " + text + " - " + version
        self.wfile.write(text.encode())


httpd = HTTPServer(('0.0.0.0', PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()