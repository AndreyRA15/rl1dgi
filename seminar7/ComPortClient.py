import serial
import helper

class ComPort():
    Connected = False
    def Connect(self, portName, baudRate, byteSize = 8, stopBits = 1):
        if(not self.Connected):
            print("Попытка установить соединение", portName)
            try:
                self.port = serial.Serial(port=portName, baudrate=baudRate, bytesize=byteSize, stopbits=stopBits)
                self.Connected = True
            except serial.SerialException:
                print("Проверьте првильность установки параметров")
            except:
                print("Вознкла другая ошибка")
            finally:
                print(("Соединение установлено" if self.Connected else "Соединение не установлено"))

    def Disconnect(self):
        self.port.close()

    def Send(self, data):
        if(self.Connected):
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
        else:
            print("Device is not connected")
        
    def ReceiveBytes(self):
        if(self.Connected):
            print("Ожидание ответа...")
            resp = self.port.read_until()
            print("Ответ получен:", resp.decode(helper.encoding))
            return resp
        else:
            print("Device is not connected")
            return b""

    def ReceiveStr(self):
        resp = self.ReceiveBytes()
        return resp.decode(helper.encoding)
    
    def Query(self, answer):
        self.Send(answer)
        return self.ReceiveStr()
    
