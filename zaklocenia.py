def negationScrambler(data):
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
            if temp > range_var-1:
                temp -= range_var
            if range_index + index2 < len(data):
                data[range_index + index2] = data_temp[temp]

def shiftDecramble(data, packet_size):
    key = 3
    range_var = int(packet_size)

    for range_index in range(0, len(data) - range_var, range_var):
        data_temp = list()
        for index in range(0, range_var):
            data_temp.append(data[index + range_index])
        for index2 in range(range_var, 0):
            temp = index2 + key
            if temp > range_var-1:
                temp -= range_var
            if range_index + index2 < len(data):
                data[range_index + index2] = data_temp[temp]



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


def negationDescrambler(data):
    index = 0
    while index < len(data):
        if data[index] == 0:
            data[index] = 1

        elif data[index] == 1:
            data[index] = 0

        index += 2

    # def repeatDescrambler(data):
