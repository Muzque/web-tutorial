import socket

HEADER = 64
PORT = 8080
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '[DISCONNECT]'
SERVER = '192.168.0.6'
ADDR = (SERVER, PORT)


def send_message(client, message: str) -> None:
    msg_encoded = message.encode(FORMAT)
    header_encoded = str(len(message)).encode(FORMAT)
    header_encoded += b' ' * (HEADER - len(header_encoded))
    client.send(header_encoded)
    client.send(msg_encoded)
    response = client.recv(2048).decode(FORMAT)
    print(f'[Response] {response}')


def send_disconnected(client) -> None:
    send_message(client, message=DISCONNECT_MESSAGE)


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    send_message(client, 'Hello World!')
    send_disconnected(client)


if __name__ == '__main__':
    main()
