from http.server import HTTPServer,BaseHTTPRequestHandler

content='''


<HTML>
    <CENTER>
    <H1>LAPTOP CONFIGURATION</H1>
</CENTER>
    <BODY>
        <CENTER>
        <TABLE border="2" CELLPADDING="10">
 <TR>
    <TD>LAPTOP NAME:</TD><TD>LENOVO LOQ</TD>
 </TR>           
<TR>
    <TD>DEVICE NAME:</TD><TD>LAPTOP-O8P3JV8H</TD>
</TR>
<TR>
    <TD>OPERATIN SYSTEM:</TD><TD>WINDOWS 11 HOME</TD>
</TR>
<TR>
    <TD>PROCESSOR:</TD><TD>AMD Ryzen 5 7235HS </TD>
</TR>
<TR>
    <TD>CLOCK SPEED:</TD><TD>Max Frequency up to 4.2 GHz</TD>
</TR>
<TR>
    <TD>INSTALLED RAM:</TD><TD>24GB RAM </TD>

</TR>
<TR>
    <TD>RAM TYPE:</TD><TD>DDR5</TD>
</TR>
<TR>
    <TD>GRAPHIC PROCESSOR:</TD><TD>NVIDIA GeForce RTX 3050</TD>
</TR>
<TR>
    <TD>SSD CAPACITY</TD><TD>512GB</TD>
</TR>
<tr>
    <td>TYPE</td><td>GAMING LAPTOP</td>
</tr>
<TR>
    <TD>POWER SUPPLY</TD><TD>170W</TD>
</TR>
</CENTER>
    </BODY>
</TABLE>
</HTML>
'''


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()