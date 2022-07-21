from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "127.0.0.1"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if(self.path == "/healthcheck"):{
        self.send_response(200),
        self.send_header("Content-type", "text/html"),
        self.end_headers(),
        self.wfile.write(bytes("<html><head><title>Test Johnny`s Web Server</title></head>", "utf-8")),
        self.wfile.write(bytes("<p> Ok </p>", "utf-8")),
        self.wfile.write(bytes("</body></html>", "utf-8"))}
        else:{
             self.send_response(404)
        }


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")