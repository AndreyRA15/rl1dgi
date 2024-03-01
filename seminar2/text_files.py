import struct
import matplotlib.pyplot as plt


with open("fileWithString.txt", "w") as file:
    file.write("Some string value!")


with open("fileWithString.txt", "r") as file:
    data = file.read()
    print(data)


bytesData = data.encode(encoding="ascii")

strDecoded = bytesData.decode(encoding="utf-16")


bytesData = data.encode(encoding="ascii")

strDecoded = bytesData.decode(encoding="utf-16")

print(strDecoded)

# file = open("fileWithString.txt", "r")
# data = file.read()
# print(data)
# file.close()


# with open("seminar1/sample-3s.wav", "rb") as file:
#     data = file.read()

# print(data)

# fileType = data[0:4].decode()



# print(fileType)

# fileSize = struct.unpack_from('i', data, offset=4)
# print(fileSize)

# pureAdcData =[a for a in struct.iter_unpack("H",data[44:])]

# print(pureAdcData)

# plt.plot(pureAdcData)
# plt.show()