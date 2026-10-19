#!/usr/bin/env python3
import http.server
import socketserver
import os
import mimetypes
import socket

DIRECTORY = os.path.dirname(os.path.abspath(__file__))

mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")
mimetypes.add_type("image/webp", ".webp")
mimetypes.add_type("model/obj", ".obj")
mimetypes.add_type("font/ttf", ".ttf")
mimetypes.add_type("audio/mpeg", ".mp3")

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

def get_free_port(start_port=8000):
    port = start_port
    while port < 65535:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
        port += 1
    return start_port

if __name__ == "__main__":
    port = get_free_port(8000)
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", port), CustomHandler) as httpd:
        print("=" * 60)
        print(f" Web thiệp DLove đang chạy tại: http://localhost:{port}")
        print(f" Thư mục dữ liệu: {DIRECTORY}")
        print(" Nhấn Ctrl+C để dừng server.")
        print("=" * 60)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nĐã dừng server.")
