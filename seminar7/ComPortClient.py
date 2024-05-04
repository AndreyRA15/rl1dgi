import serial
import helper

class ComPortClient():
    def Connect(self, portName, baudRate):
        print("Попытка установить соединение", portName)
        try:
            self.port = serial.Serial(port=portName, baudrate=baudRate)
            self.Connected = True
            print("Соединение установлено")
        except:
            self.Connected = False
            print("Соединение не установлено")


    def Send(self, data):
        if(type(data) is bytes):
            print("Отправка сообщения", data.decode(helper.encoding))
            self.port.write(data)
            print("Успешно отправлено")
        elif(type(data) is str):
            print("Отправка сообщения", data)
            self.port.write(data.encode(helper.encoding))
            print("Успешно отправлено")
        else:
            print("Поддерживаются только типы str и bytes")
        
        
    def ReceiveBytes(self):
        print("Ожидание ответа...")
        resp = self.port.read_all()
        print("Ответ получен:", resp.decode(helper.encoding))
        return resp

    def ReceiveStr(self):
        resp = self.ReceiveBytes()
        return resp.decode(helper.encoding)
    
    def Query(self, answer):
        self.Send(answer)
        return self.ReceiveStr()
    
    