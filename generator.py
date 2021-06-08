from random import shuffle
from bitarray import bitarray
from zaklocenia import negationScramble, negationDescramble
from zaklocenia import shiftScramble, shiftDescramble
from zaklocenia import multiplicativeScramble, multiplicativeDescramble
from zaklocenia import additiveScramble, additiveDescramble


def generator(size, ones_p, packet_size):
    zeros = int(size) - round(int(size) * int(ones_p) / 100, 0)
    ones = int(size) - int(zeros)

    data = bitarray()
    for i in range(0, int(zeros)):
        data.append(0)
    for j in range(0, int(ones)):
        data.append(1)
    # data = [0] * int(zeros) + [1] * int(ones)
    shuffle(data)
    print(data)
    # save(packet_size, data)

    #negationScramble(data)
    #print(data)
    #negationDescramble(data)

    shiftScramble(data, packet_size)
    print(data)
    shiftDescramble(data, packet_size)

    # multiplicativeScramble(data)
    # print(data)
    # multiplicativeDescramble(data)

    #additiveScramble(data)
    #print(data)
    #additiveDescramble(data)

    # save(packet_size, data)
    print(data)


def save(packet_size, data):
    file = open("packages.txt", "w+")  # "w+"- do zapisu i odczytu

    for index in range(1, len(data) + 1):
        file.write(str(data[index - 1]))
        if index % int(packet_size) == 0:
            file.write("\n")

    file.close()
