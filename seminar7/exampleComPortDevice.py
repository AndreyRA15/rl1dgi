from ComPortClient import ComPort
port = "COM3"


client = ComPort()
client.Connect(port, 115200)

def requestProcessing(request:str):
    if("*IDN?" in request):
        responce = "I am server on port " + str(port)
    else:
        responce = "ERROR"
    return responce + "\n"

while True:
    readMessage = client.ReceiveStr()
    sendMessage = ""
    try:
        sendMessage = requestProcessing(readMessage)
    except:
        print("Error!!!")
    finally:
        client.Send(sendMessage)
    