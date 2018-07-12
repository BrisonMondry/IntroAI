#
# file = open("train-labels-idx1-ubyte.gz",'rb')
# by = file.read()
# print(int.from_bytes(by,byteorder="big",signed=False))
#

import struct
import gzip

train_lables = gzip.open('train-labels-idx1-ubyte.gz', mode='rb')
#by = f.read()
magic = struct.unpack('>i', train_lables.read(4))
items = struct.unpack('>i', train_lables.read(4))
numbers = []

for i in range(0,items[0]):
    numbers.append(struct.unpack('>b', train_lables.read(1))[0])

for n in numbers:
    if n < 0 or n > 9:
        print('nope')

print(magic, " ", items)



