from SyncTcpClient import SyncTcpClient

client  = SyncTcpClient()
client.Connect('127.0.0.1', 30001)

print(client.Query("*IDN?\n"))
print(client.Query("*ID?\n"))
