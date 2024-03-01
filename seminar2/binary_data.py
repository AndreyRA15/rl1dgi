stringValue = "Some string value!"


bytesData = stringValue.encode(encoding="ascii")

strDecoded = bytesData.decode(encoding="ascii")

print(strDecoded)

bytesData = stringValue.encode(encoding="utf-16")

strDecoded = bytesData.decode(encoding="utf-16")

print(strDecoded)

# bytesData = stringValue.encode(encoding="ascii")

# strDecoded = bytesData.decode(encoding="utf-16")

# print(strDecoded)

import struct

pi = 3.1415

binaryPi = struct.pack('d', pi)
print(binaryPi, "Length:", len(binaryPi), "bytes")

someNumber = 100

binaryPiAndNum = struct.pack("di",pi,someNumber)

print(binaryPiAndNum, "Length:", len(binaryPiAndNum), "bytes")

unpackValues = struct.unpack("di",binaryPiAndNum)
print(unpackValues)

step = 0.2
data = [a*step for a in range(11)]

print(data)
# print(*data)

# binaryData = struct.pack(str(len(data))+'f', *data)

# print(len(binaryData))

# data1 = [a[0] for a in struct.iter_unpack("f", binaryData)]
# print(data1)

#С двойной точностью

# print(*data)

# binaryData = struct.pack(str(len(data))+'d', *data)

# print(len(binaryData))

# data1 = [a[0] for a in struct.iter_unpack("d", binaryData)]
# print(data1)