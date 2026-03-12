from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        if self.path == '/health':
            response = {'status': 'healthy', 'version': '1.0.0'}
        else:
            response = {'message': 'Hello from CI/CD project!'}
        
        self.wfile.write(json.dumps(response).encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), SimpleHandler)
    print('Server running on port 8000...')
    server.serve_forever()
