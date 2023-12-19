from socket import *

# Server setup
serverPort = 9966
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)


# Main server loop
while True:
    print("the server is ready to receive ...")
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print(" IP: " + addr[0] + " port: " + str(addr[1]))
    print(sentence)
    
    ip = addr[0]
    port = addr[1]
    
    string_list = sentence.split(' ')  # Split request by spaces
    method = string_list[0]
    requestFile = string_list[1]
    file = requestFile.split('? ')[0]
    file = file.lstrip('/ ')
    
    if file == '' or file == 'index.html' or file == 'main_en.html' or file == 'en':
        # Sending main-er.html content
        connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send(f"Content-Type: text/html\r\n\r\n".encode())
        with open('main_en.html', 'r') as f:
            connectionSocket.send(f.read().encode())
    elif file == 'ar':
        # Sending main_ar.html content with correct encoding
        with open('main_ar.html', encoding='utf-8') as f:
            html = f.read()
        connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send(f"Content-Type: text/html; charset=UTF-8\r\n\r\n".encode())
        connectionSocket.send(html.encode())
    elif file.endswith('.html'):
        # Sending HTML file content
        connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send(f"Content-Type: text/html\r\n\r\n".encode())
        with open(file, 'r') as f:
            connectionSocket.send(f.read().encode())
    elif file.endswith('.css'):
        # Sending CSS file content
        connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send(f"Content-Type: text/css\r\n\r\n".encode())
        with open(file, 'r') as f:
            connectionSocket.send(f.read().encode())
    elif file.endswith('.png'):
        # Sending PNG file content
        connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send(f"Content-Type: image/png\r\n\r\n".encode())
        with open(file, 'rb') as f:
            connectionSocket.send(f.read())
    elif file.endswith('.jpg'):
        # Sending JPEG file content
        connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send(f"Content-Type: image/jpeg\r\n\r\n".encode())
        with open(file, 'rb') as f:
            connectionSocket.send(f.read())
    elif file == "cr":
        # Redirecting to Cornell University website
        connectionSocket.send(f"HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send(f"Location: https://www.cornell.edu/\r\n\r\n".encode())
    elif file == "so":
        # Redirecting to Stack Overflow website
        connectionSocket.send(f"HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send(f"Location: https://stackoverflow.com/\r\n\r\n".encode())
    elif file == "rt":
        # Redirecting to Birzeit University registration page
        connectionSocket.send(f"HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send(f"Location: https://ritaj.birzeit.edu/register/\r\n".encode())
    else:
        # Handling exception and returning a simple HTML page with IDs
        connectionSocket.send(f"HTTP/1.1 404 Not Found\r\n".encode())
        response = (
            '<html>'
            '<title>Error 404</title>'
            '<body><center><h1 style = "color : red ;"> Error 404 : the file is Not Found</h1><hr>'
                '<p style= "font-weight: bold;">safaa taweel  1202065</p>' 
                '<p style= "font-weight: bold;">abdalrahim thiab  12020102</p>'
                '<hr><h2>Client IP: '+ str(ip) + ', Port Number: ' + str(port)+ 
                '</h2></center></body></html>').encode('utf-8')

        connectionSocket.send(f"\r\n".encode())
        connectionSocket.send(response)
        connectionSocket.close()
