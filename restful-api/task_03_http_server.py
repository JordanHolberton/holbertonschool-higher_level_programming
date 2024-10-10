#!/usr/bin/python3
"""
Simple HTTP server using http.server to handle GET requests.
This server responds to three endpoints:
- '/' : Returns a simple text message.
- '/data': Returns a JSON response with sample data.
- '/info': Returns a JSON response with version info.
"""

import http.server
import json

PORT = 8000
Handler = http.server.BaseHTTPRequestHandler


class Server(Handler):
    """
    Custom HTTP server handler to manage different GET endpoints.
    """

    def do_GET(self):
        """
        Handle GET requests.
        Routes:
        - "/" returns a plain text response.
        - "/data" returns a JSON object with user data.
        - "/info" returns a JSON object with API information.
        """
        if self.path == '/':
            # Response for the root endpoint
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            # Response for the /data endpoint
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == "/info":
            # Response for the /info endpoint
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            # Response for an unknown endpoint
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    # Create the server, binding to localhost on port 8000
    with http.server.HTTPServer(("", PORT), Server) as httpd:
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()
