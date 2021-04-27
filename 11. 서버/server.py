'''
1. 소켓 생성
2. 바인딩
3. 접속 대기
4. 접속 수락
5. 데이터 송수신
6. 접속 종료
'''

import socket

print("1. 소켓 생성")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP를 사용함

print("2. 바인딩")
sock.bind(("localhost", 6325))

print("3. 접속 대기")
sock.listen()

print("4. 접속 수락")
c_sock, addr = sock.accept() #클라이언트 소켓, 주소가 리턴됨.

print("5. 데이터 송수신")
receiveData = c_sock.recv(1024).decode()
print("수신된 데이터: {}".format(receiveData))

print("6. 접속 종료")
c_sock.close()
sock.close()