import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from time import strftime


class CS2610Assn1(BaseHTTPRequestHandler):
    def write_html(self, html: str):
        self.wfile.write(bytes(html, "utf-8"))

    def write_headers(self, code):
        if code == 200:
            self.send_response(200)
        if code == 301:
            self.send_response(301)
        if code == 404:
            self.send_response(404)
        if code == 403:
            self.send_response(403)
        if code == 418:
            self.send_response(418)
        self.send_header("Connection", "close")
        self.send_header("Cache-Control", "max-age=5")

    def serve_file(self, filename: str, headers: bool, use_layout=False):

        if headers:
            self.write_headers(200)
            if filename.__contains__(".html"):
                self.send_header("Content-type", "text/html")
            elif filename.__contains__(".css"):
                self.send_header("Content-type", "text/css")
            elif filename.__contains__(".ico"):
                self.send_header("Content-type", "image/icon")
            elif filename.__contains__(".jpg"):
                self.send_header("Content-type", "image/jpeg")
            elif filename.__contains__(".png"):
                self.send_header("Content-type", "image/png")
        f = open(filename, "rb")
        data = f.read()  # slurping the entire file at once
        f.close()
        if headers:
            if use_layout and filename.__contains__(".html"):
                top_layout = os.stat("layout/_LayoutTop.html").st_size
                bottom_layout = os.stat("layout/_LayoutBottom.html").st_size
                self.send_header("Content-Length", (len(data) + top_layout + bottom_layout).__str__())
            else:
                self.send_header("Content-Length", len(data).__str__())
            self.end_headers()
        if use_layout and filename.__contains__(".html"):
            self.serve_file("layout/_LayoutTop.html", False)
        self.wfile.write(data)
        if use_layout and filename.__contains__(".html"):
            self.serve_file("layout/_LayoutBottom.html", False)

    def do_GET(self):
        print(f"Got a request to {self.path}")
        if self.path == "/404.html":
            self.write_headers(200)
            self.end_headers()
            self.serve_file("404.html", False, True)
        elif self.path == "/forbidden":
            self.write_headers(403)
            self.end_headers()
            self.serve_file("forbidden.html", False, True)
        elif self.path == "/teapot":
            self.write_headers(418)
            self.end_headers()
            self.serve_file("layout/_LayoutTop.html", False)
            self.write_html("<img src='./images/teapot.jpg' alt='teapot' style='width:100%'>")
            self.serve_file("layout/_LayoutBottom.html", False)
        elif Path(self.path[1:]).is_file():
            self.serve_file(self.path[1:], True, True)
        elif Path(self.path[1:] + ".html").is_file():
            self.write_headers(301)
            self.send_header("Location", self.path[1:] + ".html")
            self.end_headers()
        elif self.path == "/" or self.path == "/index" or self.path == "/index.htm":
            self.write_headers(301)
            self.send_header("Location", "/index.html")
            self.end_headers()
        elif self.path.lower().startswith("/bio"):
            self.write_headers(301)
            self.send_header("Location", "/about.html")
            self.end_headers()
        elif self.path == "/debugging":
            self.write_headers(200)
            self.end_headers()
            self.serve_file("layout/_LayoutTop.html", False)
            self.write_html("""
                                    <p>This is my debugging page!</p>
                                    <p> The version string is: """ + self.version_string() + """
                                    <p>The current date and time is: """ + strftime('%c') + """
                                    <p>Your ip is: """ + self.address_string() + """
                                    <p> The path you requested was: """ + self.path + """
                                    <p> Your request type: """ + self.command + """
                                    <p> The HTTP version of this request is: """ + self.request_version + """
                                    
                                    
                            """)
            self.write_html("<p>The HTTP request headers sent by the browser for this page are:</p><ol>")
            for header in self.headers:
                self.write_html(f"<li><p>{header} => {self.headers[header]}</p></li>")
            self.write_html("</ol>")
            self.serve_file("layout/_LayoutBottom.html", False)
        elif self.path == "/tips" or self.path == "/help":
            self.write_headers(301)
            self.send_header("Location", "/techtips+css.html")
            self.end_headers()
        else:
            self.write_headers(404)
            self.end_headers()
            self.serve_file("404.html", False, True)
        pass


if __name__ == '__main__':
    server_address = ('localhost', 8000)
    print(f"Serving from http://{server_address[0]}:{server_address[1]}")
    print("Press Ctrl-C to quit\n")
    try:
        HTTPServer(server_address, CS2610Assn1).serve_forever()
    except KeyboardInterrupt:
        print(" Exiting")
        exit(0)
