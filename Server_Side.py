import socket, cv2, pickle,struct
#To create socket instance
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)

port = 5555
socket_address = ('192.168.0.104',port)
print("Socket Created")

#To bind the socket 
server_socket.bind(socket_address)
print("Socket Bind Successfully")

#To make socket ready for accepting connections. 
server_socket.listen(5)
print("Listening At:",socket_address)

#To accept the connection request from the client.
print("Socket Accept")
while True:
    client_socket,addr = server_socket.accept()
    print('Got Connected With:',addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        
        while(vid.isOpened()):
            img,frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            
            cv2.imshow('Video Transmitting ',frame)
            key = cv2.waitKey(1) & 0xFF
            if key ==ord('q'):
                client_socket.close()

