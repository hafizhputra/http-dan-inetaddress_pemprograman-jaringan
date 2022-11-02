import ctypes
from dataclasses import field
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
# import sys

menumakanan = ['Nasi Goreng','Nasi Rendang', 'Ayam Geprek']

class webserverHandler(BaseHTTPRequestHandler):
    """docstring untuk webserverHandler"""



    def do_GET(self):

            local="localhost:8080"

            if self.path.endswith("/list"):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()

                output = ""
                output += '<html><body style="background-color:black">'
                output += '<h1 style="color:white;text-align: center;margin-top:9%;font-size:3rem">Menu Makanan</h1>'
                output += '<div style="background-color:white;margin-right:30%;margin-left:30%;padding-bottom:6%;border-radius:15px;padding-top:0.40%;">'
                for menu in menumakanan:
                  output += '<p style="display: block; margin-left:2%;">'
                  output += menu 
                  output += '</p>'
                
                output += '</div >'
                output += '</br>'
                output += '<h3 style="text-align: center; "><button style="width: 40%; padding-top:0.50%;padding-bottom:0.50%;border-radius:15px"><a href=/list/tambah style="font-size:1.40rem;text-decoration: none;color:black;">Tambah Menu</a></button></h3>'
                output += '</body></html>'

                self.wfile.write(output.encode())
                # print(output)
                # return

            elif self.path.endswith("/tambah"):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()

                output = ""
                output += '<html><body style="background-color:black">'
                output += '<h1 style="color:white;text-align: center;margin-top:15%;font-size:3rem">Tambah Menu Makanan</h1>'

                output += '<form method="POST" enctype="multipart/form-data" action="/list/tambah" style="text-align: center;">'
                output += '<input name="menu" type="text" placeholder="tambahkan menu makanan" style="width: 35%;padding: 12px 20px;margin: 8px 0;display: inline-block;border: 1px solid #ccc;border-radius: 4px;box-sizing: border-box;">'
                # output += '<button type="submit" value="tambah" style="display: block;width: 100%;text-align: center;" >Simpan</button>'
                output += '<h3 style="text-align: center; " ><button type="submit" value="tambah" style="width: 35%; padding-top:0.50%;padding-bottom:0.50%;border-radius:15px"><a style="font-size:1.40rem;text-decoration: none;color:black;">Tambah Menu</a></button></h3>'
                output += '</form>'
                output += '</body></html>'
                self.wfile.write(output.encode())

            else:
                self.path.endswith(local)
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()

                output = ""
                output += '<html>'
                output += '<body style="background-color:black">'
                output += '<h1 style="text-align: center;color:white;margin-top:15%;font-size:3rem;">Tersambung Cuy!!</h1>'
                output += '</br>'
                output += '<h1 style="text-align: center;"><button><a href=/list style="font-size:2rem;text-decoration: none;color:black;">Next</a></button></h1>'
                output += '</body></html>'

                self.wfile.write(output.encode())    

    def do_POST(self):
      
            if self.path.endswith("/tambah"):
                ctype,pdict = cgi.parse_header(self.headers.get('content-type'))
                pdict['boundary'] = bytes(pdict['boundary'],"utf-8")
                
                #menambah content_leng (html)
                content_len = int(self.headers.get('Content-length'))
                pdict['CONTENT-LENGTH'] = content_len

                if ctype == 'multipart/form-data':
                  fields = cgi.parse_multipart(self.rfile, pdict)
                  # get dari name form (name="menu")
                  new_menu = fields.get('menu')
                  # ngambil dari array 
                  menumakanan.append(new_menu[0])

                self.send_response(301)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Location','/list')
                self.end_headers()

              
                

def main():
    try:
        port = 8080
        server = HTTPServer(('localhost', port), webserverHandler)
        print("Web server running on port %s" % port)
        server.serve_forever()

    except KeyboardInterrupt:
        print(" ^C entered stopping web server...")
        server.socket.close()



if __name__ == '__main__':
    main()