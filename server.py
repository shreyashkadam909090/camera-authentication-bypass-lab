from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse
import base64

USERNAME = "admin"
PASSWORD = "1234"

class Handler(SimpleHTTPRequestHandler):

    # check login session
    def is_logged_in(self):
        cookie = self.headers.get("Cookie")
        return cookie and "session=1" in cookie

    def do_GET(self):

        # redirect root → login page
        if self.path == "/" or self.path == "/login":
            self.send_response(302)
            self.send_header("Location", "/login.html")
            self.end_headers()
            return

        # protect viewer page
        if self.path == "/viewer.html":
            if not self.is_logged_in():
                self.send_response(302)
                self.send_header("Location", "/login.html")
                self.end_headers()
                return

        return super().do_GET()

    def do_POST(self):

        # 🔐 LOGIN HANDLER
        if self.path == "/login":
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length).decode()

            form = urllib.parse.parse_qs(data)
            user = form.get("username", [""])[0]
            pw = form.get("password", [""])[0]

            # ❌ empty fields
            if not user or not pw:
                self.send_response(302)
                self.send_header("Location", "/login.html?error=empty")
                self.end_headers()
                return

            # ❌ wrong credentials
            if user != USERNAME or pw != PASSWORD:
                self.send_response(302)
                self.send_header("Location", "/login.html?error=wrong")
                self.end_headers()
                return

            # ✅ correct login
            self.send_response(302)
            self.send_header("Set-Cookie", "session=1; Path=/")
            self.send_header("Location", "/viewer.html")
            self.end_headers()
            return

        # 📸 CAMERA UPLOAD
        if self.path == "/upload":
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length)

            try:
                image_data = data.split(b",")[1]
                image = base64.b64decode(image_data)

                with open("frame.jpg", "wb") as f:
                    f.write(image)

                self.send_response(200)
                self.end_headers()

            except Exception as e:
                print("Error:", e)
                self.send_response(500)
                self.end_headers()

PORT = 8000
print(f"Server running on http://0.0.0.0:{PORT}")

HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()