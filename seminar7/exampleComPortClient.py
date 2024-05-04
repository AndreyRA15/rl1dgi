from ComPortClient import ComPort


client = ComPort()
client.Connect("COM7", 115200)

client.Query("*IDN?\n")