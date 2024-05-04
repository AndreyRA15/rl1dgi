from ComPortClient import ComPortClient


client = ComPortClient()
client.Connect("COM4", 115200)

client.Query("Temp String")