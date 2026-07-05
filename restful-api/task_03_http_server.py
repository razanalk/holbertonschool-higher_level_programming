#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPI(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/":

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(
                b"Hello, this is a simple API!"
            )

        elif self.path == "/data":

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.send_response(200)
            self.send_header(
                "Content-type",
                "application/json"
            )
            self.end_headers()

            self.wfile.write(
                json.dumps(data).encode()
            )

        elif self.path == "/status":

            self.send_response(200)
            self.send_header(
                "Content-type",
                "text/plain"
            )
            self.end_headers()

            self.wfile.write(b"OK")

        else:

            self.send_response(404)
            self.send_header(
                "Content-type",
                "text/plain"
            )
            self.end_headers()

            self.wfile.write(
                b"Endpoint not found"
            )


def run():

    server = HTTPServer(
        ("localhost", 8000),
        SimpleAPI
    )

    print("Server running on port 8000...")

    server.serve_forever()


if __name__ == "__main__":
    run()
