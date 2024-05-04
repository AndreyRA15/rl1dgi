from ComPortClient import ComPort


client = ComPort()
client.Connect("COM4", 115200)

client.Query("IDN?\n")