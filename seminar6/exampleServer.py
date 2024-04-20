from SyncTcpServer import SyncTcpServer

port = 30001

def requestProcessing(request:str):
    if("*IDN?" in request):
        responce = "Server on port " + str(port)
    else:
        responce = "ERROR"
    return responce

server = SyncTcpServer(port)
server.returnFunc = requestProcessing
server.WaitClients()