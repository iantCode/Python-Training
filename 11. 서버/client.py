'''
1. 소켓 생성
2. 
3. 접속 시도
4. 
5. 데이터 송수신
6. 접속 종료
'''

import socket

print("1. 소켓 생성")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("3. 접속 시도")
sock.connect(("localhost", 6325))

print("5. 데이터 송수신")
sock.sendall("Hello, Socket!".encode())

print("6. 접속 종료")
sock.close()