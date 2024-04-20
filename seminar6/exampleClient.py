from SyncTcpClient import SyncTcpClient

from helper import *

client  = SyncTcpClient()
client.Connect('127.0.0.1', 30001)

print(client.Query(idnCommand))
# print(client.Query("IDN?\n"))
