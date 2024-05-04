from ComPortClient import ComPortClient


client = ComPortClient()
client.Connect("COM5", 115200)

print(client.ReceiveStr())
client.Send("I am Server!")