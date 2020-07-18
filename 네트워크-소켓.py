# 소켓 라이브러리
import socket
# socket 함수를 이용하여 소켓 생성
# 매개변수에서 AF_INET은 인터넷을 통해서 나간다는 뜻
# SOCKET_STREAM은 데이터가 블록 형태가 아닌 연속된 문자의 흐름으로 다루어진다는 뜻
mysock=socket.socket(socket.AF_INET,socket.SOCKET_STREAM)
# mysocket에 저장되어 있는 소켓 객체를 가져와 인터넷을 통해 연결 만듦
# 전화로 비유하면, host인 data.pr4e.org로 전화를 걸어 내선번호인 포드 80번으로 연결을 뜻 함.
mysock.connect(('data.pr4e.org',80))
# 실행하려면 아나콘다 설치 필요
