#
# file = open("train-labels-idx1-ubyte.gz",'rb')
# by = file.read()
# print(int.from_bytes(by,byteorder="big",signed=False))
#

import struct
import gzip

train_lables = gzip.open('train-labels-idx1-ubyte.gz', mode='rb')
train_images = gzip.open('train-images-idx3-ubyte.gz', mode='rb')

magic_train_labels = struct.unpack('>i', train_lables.read(4))
num_train_labels = struct.unpack('>i', train_lables.read(4))
numbers = []

magic_train_images = struct.unpack('>i', train_images.read(4))[0]
num_train_images = struct.unpack('>i', train_images.read(4))[0]
train_img_rows = struct.unpack('>i', train_images.read(4))[0]
train_img_cols = struct.unpack('>i', train_images.read(4))[0]

print('''magic number: {}
number of images: {}
rows: {}
columns: {}\n'''.format(magic_train_images, num_train_images, train_img_rows, train_img_cols))


for i in range(0, num_train_labels[0]):
    numbers.append(struct.unpack('>b', train_lables.read(1))[0])

for n in numbers:
    if n < 0 or n > 9:
        print('nope')

print(magic_train_labels, " ", num_train_labels)



