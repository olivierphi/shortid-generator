import json
from string import Template
from http.server import BaseHTTPRequestHandler

from backend import shortid_generator

_HTML_TEMPLATE = Template("""<html>
<head>
    <title>Short unique ID - one unique ID per second.</title>
    <style>
        html {
            font-family: sans-serif;
            font-size: 16px;
        }
        body {
            height: 100%;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        main {
            text-align: center;
        }
    </style>
</head>
<body>
    <main>
        ${SHORT_ID}
    </main>
</body>
</html>
""")

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("X-Generated-by", "a Python serverless function, managed by Vercel")
        self.send_header("X-Requested-Path", self.path)
        self.send_header("X-Request-Headers", json.dumps(self.headers.items()))
        self.end_headers()
        message = _HTML_TEMPLATE.safe_substitute(SHORT_ID=shortid_generator.get_shortid())
        self.wfile.write(message.encode())
        
    def do_POST(self):
        return self.do_GET()
