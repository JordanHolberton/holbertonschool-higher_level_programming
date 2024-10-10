#!/usr/bin/python3
import http.server
import json

PORT = 8000
Handler = http.server.BaseHTTPRequestHandler

class Server(Handler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path =="/data":

            data = {"name": "John", "age": 30, "city": "New York"}  
          
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == "/info":

            info = {"version": "1.0", "description": "A simple API built with http.server"}

            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")



if __name__ == "__main__":
    # Create the server, binding to localhost on port 8000
    with http.server.HTTPServer(("", PORT), Server) as httpd:
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()
