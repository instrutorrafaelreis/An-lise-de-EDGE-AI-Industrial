"""
Servidor Local Zero-Dependencias para TV Box (Termux) ou Notebook Windows
Garante permissao total de Webcam USB via http://localhost:8080/ABRIR_NA_TVBOX.html (100% Offline)
"""
import http.server
import socketserver
import webbrowser
import os

PORT = 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = f"http://localhost:{PORT}/ABRIR_NA_TVBOX.html"
    print("=" * 72)
    print("  SISTEMA EDGE AI FRIGORIFICO SIF - MODO PENDRIVE OFFLINE ATIVO!")
    print(f"  Acesse no navegador da TV Box ou PC: {url}")
    print("=" * 72)
    try:
        webbrowser.open(url)
    except Exception:
        pass
    httpd.serve_forever()
