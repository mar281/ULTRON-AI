
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from brain import ask_ultron
from memory import save_memory

HOST = "127.0.0.1"
PORT = 5000

WEBSITE = "https://mar281.github.io"


class UltronHandler(BaseHTTPRequestHandler):

    def send_json(self, status, data):
        response = json.dumps(data).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", WEBSITE)
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", WEBSITE)
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        if self.path != "/chat":
            self.send_json(404, {"error": "Endpoint not found"})
            return

        try:
            length = int(self.headers.get("Content-Length", 0))

            if length <= 0 or length > 10000:
                self.send_json(400, {"error": "Invalid message size"})
                return

            data = json.loads(self.rfile.read(length))
            message = data.get("message", "").strip()

            if not message:
                self.send_json(400, {"error": "Message is empty"})
                return

            answer = ask_ultron(message)
            save_memory(message, answer)

            self.send_json(200, {"reply": answer})

        except Exception as error:
            self.send_json(500, {"error": str(error)})


if __name__ == "__main__":
    print("=" * 40)
    print("       ULTRON AI BACKEND")
    print("=" * 40)
    print("Server: http://127.0.0.1:5000")
    print("Status: ONLINE")
    print("Press CTRL+C to stop")

    server = HTTPServer((HOST, PORT), UltronHandler)
    server.serve_forever()
