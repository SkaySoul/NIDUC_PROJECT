from random import shuffle
from bitarray import bitarray


# funkcja generująca sygnał
def generate(size, ones_p, packet_size):
    zeros = int(size) - round(int(size) * int(ones_p) / 100, 0)
    ones = int(size) - int(zeros)

    data = bitarray()
    for i in range(0, int(zeros)):
        data.append(0)
    for j in range(0, int(ones)):
        data.append(1)

    shuffle(data)

    return data
