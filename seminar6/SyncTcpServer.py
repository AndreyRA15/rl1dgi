import socket

import helper

class SyncTcpServer():
    def __init__(self, port) -> None:
        self.Host = '127.0.0.1'
        self.Port = port
        self.SocketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SocketServer.bind((self.Host, self.Port))
        self.SocketServer.listen()
        # self.returnFunc = lambda x: "Hello, client!".encode()

    def WaitClients(self):
        print('Сервер ожидает подключения')
        self.currentClient, self.currentClientAddress = self.SocketServer.accept()
        self.ReceiveData()

    def ReceiveData(self):
        while True:
            data = self.currentClient.recv(1024**2).decode(helper.encoding)
            if not data:
                self.WaitClients()
            print("Получены от", self.currentClientAddress , "данные", str(data))
            answer = self.returnFunc(data)
            # if(type(answer) is str):
            #     answer = answer.encode(helper.encoding)
            # self.currentClient.send(answer)
            self.currentClient.send("Hello, client!".encode(helper.encoding))


# def echoFunc(data:str):
#     return data

if __name__ == '__main__':
    server = SyncTcpServer(30001)
    # server.returnFunc = echoFunc
    server.WaitClients()