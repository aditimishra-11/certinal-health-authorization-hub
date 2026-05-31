#!/usr/bin/env python3
"""Static server for the Certinal case study that sends no-cache headers, so the
browser never serves a stale index.html / styles.css during iteration."""
import http.server
import socketserver

DIRECTORY = "/Users/mehulmathur/certinal-case-study"
PORT = 4599


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), NoCacheHandler) as httpd:
        print(f"Serving {DIRECTORY} on http://localhost:{PORT} (no-cache)")
        httpd.serve_forever()
