import http.server
import socketserver
import psycopg2
import urllib.parse

# Bug: 3 post requests instead of one ???


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        query_str = self.rfile.read(content_length).decode("UTF-8")
        query_dict = urllib.parse.parse_qs(query_str)
        firstname = query_dict.get("firstname")[0]
        lastname = query_dict.get("lastname")[0]
        age = query_dict.get("age")[0]

        con = psycopg2.connect(database="database", host="localhost", port="5432")
        print("Database opened successfully")
        cur = con.cursor()
        cur.execute(
            f"""
        INSERT INTO test(name,last_name,age) VALUES('{firstname}','{lastname}','{age}');
        """
        )
        con.commit()
        con.close()
        self.send_response(200)
        self.end_headers


PORT = 8001


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
