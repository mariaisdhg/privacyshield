import http.server
import socketserver
import re
from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs

# Define constants
HOST, PORT = "localhost", 8080

# Tracking script patterns to block
TRACKING_PATTERNS = [
    re.compile(r"google-analytics\.com"),
    re.compile(r"facebook\.net"),
    re.compile(r"doubleclick\.net"),
    re.compile(r"ads\."),
    re.compile(r"track\."),
]

class PrivacyShieldRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        # Check request path against tracking patterns
        if any(pattern.search(parsed_url.netloc) for pattern in TRACKING_PATTERNS):
            self.respond_with_block()
        else:
            self.manage_cookies()
            super().do_GET()

    def manage_cookies(self):
        if "Cookie" in self.headers:
            cookie = SimpleCookie(self.headers["Cookie"])
            # Modify cookies to enhance privacy
            for key in cookie.keys():
                cookie[key]["httponly"] = True
                cookie[key]["secure"] = True
            self.headers["Cookie"] = cookie.output(header="", sep=";")
    
    def respond_with_block(self):
        self.send_response(403)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Blocked</h1><p>This tracking request has been blocked for your privacy.</p></body></html>")

def run(server_class=http.server.HTTPServer, handler_class=PrivacyShieldRequestHandler):
    server_address = (HOST, PORT)
    httpd = server_class(server_address, handler_class)
    print(f"PrivacyShield running on {HOST}:{PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()