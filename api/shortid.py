from backend import shortid_generator

from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        message = shortid_generator.get_shortid()
        self.wfile.write(message.encode())
        return
