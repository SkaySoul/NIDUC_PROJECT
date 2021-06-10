from random import shuffle
from bitarray import bitarray
from zaklocenia import negationScramble, negationDescramble
from zaklocenia import shiftScramble, shiftDescramble
from zaklocenia import multiplicativeScramble, multiplicativeDescramble
from zaklocenia import additiveScramble, additiveDescramble
from analiza import stats
from odbiornik import packetDetector


# główna funkcja sterująca programem
def generate(size, ones_p, packet_size):
    zeros = int(size) - round(int(size) * int(ones_p) / 100, 0)
    ones = int(size) - int(zeros)

    data = bitarray()
    for i in range(0, int(zeros)):
        data.append(0)
    for j in range(0, int(ones)):
        data.append(1)

    shuffle(data)
    print(data)

    # negationScramble(data)
    # print(data)
    # negationDescramble(data)

    # shiftScramble(data, packet_size)
    # print(data)
    # shiftDescramble(data, packet_size)

    multiplicativeScramble(data)
    stats(data, packet_size, ones_p)
    print(data)
    multiplicativeDescramble(data)

    # additiveScramble(data)
    # print(data)
    # additiveDescramble(data)

    # save(packet_size, data)

    # packetDetector(data, packet_size)

    print(data)

