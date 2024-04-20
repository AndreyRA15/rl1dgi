import socket

import helper

class SyncTcpClient():
    def __init__(self):
        self.SocketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def Connect(self, serverAddress, serverPort):
        self.Host = serverAddress
        self.Port = serverPort
        print("Попытка установить соединение")
        self.SocketClient.connect((self.Host, self.Port))
        print("Соединение установлено")

    def Disconnect(self):
        print("Разрыв соединения")
        self.SocketClient.close()

    def Send(self, dataBytes):
        if(type(dataBytes) is bytes):
            print("Отправка сообщения", dataBytes.decode(helper.encoding))
            self.SocketClient.sendall(dataBytes)
            print("Успешно отправлено")
        elif(type(dataBytes) is str):
            print("Отправка сообщения", dataBytes)
            self.SocketClient.sendall(dataBytes.encode(helper.encoding))
            print("Успешно отправлено")
        else:
            print("Поддерживаются только типы str и bytes")
        
    def Receive(self):
        print("Ожидание ответа...")
        resp = self.SocketClient.recv(1024**2)
        print("Ответ получен:", resp.decode(helper.encoding))
        return resp
    
    def Query(self, answer):
        self.Send(answer)
        return self.Receive()



if __name__ == '__main__':
    client = SyncTcpClient()
    client.Connect('127.0.0.1', 30001)
    client.Query(b'Hello server1')


