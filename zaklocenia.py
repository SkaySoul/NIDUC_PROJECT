from bitarray import bitarray
from bitarray.util import int2ba


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


def shiftScramble(data, packet_size):
    key = 3
    range_var = int(packet_size)

    for range_index in range(0, len(data) - range_var, range_var):
        data_temp = list()
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

    for range_index in range(0, len(data) - range_var, range_var):
        data_temp = list()
        for index in range(0, range_var):
            data_temp.append(data[index + range_index])
        for index2 in range(range_var, 0):
            temp = index2 + (range_var - key)
            if temp > range_var - 1:
                temp -= range_var
            if range_index + index2 < len(data):
                data[range_index + index2] = data_temp[temp]


Index1 = 5
Index2 = 10


def multiplicativeScramble(data):
    current_index = Index2

    while current_index < len(data):
        data[current_index] = data[current_index] ^ (data[current_index - Index1] ^ data[current_index - Index2])
        current_index += 1


# TODO stworzyć inne scrabmlery 


def multiplicativeDescramble(data):
    current_index = Index2
    temp = data.copy()

    while current_index < len(temp):
        data[current_index] = temp[current_index] ^ (temp[current_index - Index1] ^ temp[current_index - Index2])
        current_index += 1


# xor - nie działa - jakiś błąd '^ - binary xor'
# seed musi być podzielny przez długość sygnału


# Polynomial 1+z^(-3)+z^(4)+z^(-7)
def XORKeyGenerator(seed):
    generatedKey = seed

    generatedKey ^= generatedKey >> 3
    generatedKey ^= generatedKey << 2
    generatedKey ^= generatedKey >> 7
    # print(int2ba(generatedKey))
    return int2ba(generatedKey)


def additiveScramble(data):
    current_index = 0
    #scramble_key = int2ba(int(len(data)/2))
    scramble_key = XORKeyGenerator(5)

    while current_index < len(data) - 1:
        data[current_index:(current_index + len(scramble_key))] = data[current_index:(current_index + len(scramble_key))] ^ scramble_key
        current_index += len(scramble_key)


def additiveDescramble(data):
    current_index = 0
    temp = data.copy()
    #scramble_key = int2ba(int(len(data)/2))
    scramble_key = XORKeyGenerator(5)

    while current_index < len(temp) - 1:
        data[current_index:(current_index + len(scramble_key))] = temp[current_index:(current_index + len(scramble_key))] ^ scramble_key
        current_index += len(scramble_key)


# TODO stworzyć inne scrabmlery

# TODO  Zliczyć ile w pakiecie występuje niezmiennych sekwencji różnej długości np. w pakiecie 100111  mamy 0*2 i 1*3 i w zależnośći od wystąpień przy sobie zwiększamy prawdopodobieństwo zepsucia pakietu
# TODO losujemy prawdopodobieństwo czy pakiet jest popsuty

def repeatCounter(data):
    reps_0 = 0
    reps_1 = 0
    for index in range(0, len(data)):
        if data[index] == 0:
            reps_0 += 1
            reps_1 = 0

            if reps_0 == 3:
                data[index] = 1
                reps_0 = 0

        if data[index] == 1:
            reps_1 += 1
            reps_0 = 0

            if reps_1 == 3:
                data[index] = 0
                reps_1 = 0
