from ComPortClient import ComPortClient
port = "COM5"


client = ComPortClient()
client.Connect(port, 115200)

def requestProcessing(request:str):
    if("*IDN?" in request):
        responce = "I am server on port " + str(port)
    else:
        responce = "ERROR"
    return responce

while True:
    readMessage = client.ReceiveStr()
    try:
        sendMessage = requestProcessing(readMessage)
    except:
        print("Error!!!")
    finally:
        client.Send(sendMessage + "\n")
    