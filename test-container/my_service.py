from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
from sys import argv

PORT = 8000
script, label = argv
version = "NA"

with open('git-hash.txt') as reader:
    version = reader.read()

print ("starting my_service, version: " + version + " and label: " + label)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        current_time = str(datetime.datetime.now())
        text = label + " - " + current_time + " - " + version
        self.wfile.write(text.encode())


httpd = HTTPServer(('0.0.0.0', PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()