import struct
# import matplotlib.pyplot as plt




with open("sample-3s.wav", "rb") as file:
    data = file.read()

# print(data)

fileType = data[0:4].decode()

print(fileType)

fileSize = struct.unpack_from('i', data, offset=4)
print(fileSize)

# pureAdcData =[a for a in struct.iter_unpack("H",data[44:])]

# print(pureAdcData)

# plt.plot(pureAdcData)
# plt.show()

