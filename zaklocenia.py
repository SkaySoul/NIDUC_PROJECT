from bitarray import bitarray
from bitarray.util import int2ba


# negacja co 2 bitu
def negationScramble(data):
    index = 0
    while index < len(data):
        if data[index] == 0:
            data[index] = 1

        elif data[index] == 1:
            data[index] = 0

        index += 2


def negationDescramble(data):
    index = 0
    while index < len(data):
        if data[index] == 0:
            data[index] = 1

        elif data[index] == 1:
            data[index] = 0

        index += 2


# przesunięcie o 3 pozycje
def shiftScramble(data, packet_size):
    key = 3
    range_var = int(packet_size)

    for range_index in range(0, len(data) - range_var + 1, range_var):
        data_temp = bitarray()
        for index in range(0, range_var):
            data_temp.append(data[index + range_index])
        for index2 in range(0, range_var):
            temp = index2 + key
            if temp > range_var - 1:
                temp -= range_var
            if range_index + index2 < len(data):
                data[range_index + index2] = data_temp[temp]


def shiftDescramble(data, packet_size):
    key = 3
    range_var = int(packet_size)

    for range_index in range(0, len(data) - range_var + 1, range_var):
        data_temp = bitarray()
        for index in range(0, range_var):
            data_temp.append(data[index + range_index])
        for index2 in range(0, range_var):
            temp = index2 + (range_var - key)
            if temp > range_var - 1:
                temp -= range_var
            if range_index + index2 < len(data):
                data[range_index + index2] = data_temp[temp]


Index1 = 5
Index2 = 10


# operacja XOR pomiędzy badaną pozycją a wybranymi pozycjami przesuniętymi w lewo
def multiplicativeScramble(data):
    current_index = Index2

    while current_index < len(data):
        data[current_index] = data[current_index] ^ (data[current_index - Index1] ^ data[current_index - Index2])
        current_index += 1


def multiplicativeDescramble(data):
    current_index = Index2
    temp = data.copy()

    while current_index < len(temp):
        data[current_index] = temp[current_index] ^ (temp[current_index - Index1] ^ temp[current_index - Index2])
        current_index += 1


# długość seeda w NB musi być podzielna przez długość długości sygnału w NB
# 66 = 1000010 (7) | 8856 = 10001010011000 (14)

def keyGenerator(seed):
    generated_key = seed

    # wzór: 1+z^(-3)+z^(4)+z^(-5)
    generated_key ^= generated_key >> 3
    generated_key ^= generated_key << 4
    generated_key ^= generated_key >> 5
    return int2ba(generated_key)


# operacja XOR pomiędzy częścią sygnału a wygenerowanym kluczem
def additiveScramble(data):
    current_index = 0
    scramble_key = keyGenerator(66)

    while current_index < len(data) - 1:
        data[current_index:(current_index + len(scramble_key))] = data[current_index:(
                current_index + len(scramble_key))] ^ scramble_key
        current_index += len(scramble_key)


def additiveDescramble(data):
    current_index = 0
    temp = data.copy()
    scramble_key = keyGenerator(66)

    while current_index < len(temp) - 1:
        data[current_index:(current_index + len(scramble_key))] = temp[current_index:(
                current_index + len(scramble_key))] ^ scramble_key
        current_index += len(scramble_key)
