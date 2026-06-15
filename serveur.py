from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import time
import json

class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def do_GET(self):
        if self.path == "/":
            with open("test_connexion.html", "rb") as f:
                contenu = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(contenu)

        elif self.path == "/serveurs":
            # Récupère les URLs Fast.com et les renvoie au navigateur
            r = requests.get(
                "https://api.fast.com/netflix/speedtest/v2"
                "?https=true&token=YXNkZmFzZGxmbnNkYWZoYXNkZmhrYWxm"
                "&urlCount=8",
                timeout=10
            )
            data = r.json()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

print("Serveur démarré sur http://localhost:8080")
HTTPServer(("", 8080), Handler).serve_forever()