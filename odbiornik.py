from random import randint
import math


# TODO poprawa funkcji wyznaczającej prawdopodobieństwo zepsucia


# zliczanie wystąpień i detekcja popsutych pakietów
def packetDetector(data, packet_length):
    good_packets = 0
    bad_packets = 0

    temp = 0
    for repeats in range(0, int(len(data) / int(packet_length))):

        reps_1 = 0
        reps_1_max = 0
        reps_0 = 0
        reps_0_max = 0

        for index in range(0, int(packet_length)):
            if data[temp + index] == 0:
                reps_0 += 1
                if reps_1_max < reps_1:
                    reps_1_max = reps_1
                reps_1 = 0

            if data[temp + index] == 1:
                reps_1 += 1
                if reps_0_max < reps_0:
                    reps_0_max = reps_0
                reps_0 = 0

            if index == (int(packet_length) - 1):
                if reps_1_max < reps_1:
                    reps_1_max = reps_1
                if reps_0_max < reps_0:
                    reps_0_max = reps_0

        if corruptionProbability(reps_1_max, reps_0_max, packet_length):
            bad_packets += 1
        else:
            good_packets += 1
        temp += int(packet_length)

    return bad_packets


# prawdopodobieństwo zepsucia pakietu
def corruptionProbability(reps_1, reps_0, packet_length):
    probability = 0
    probability += reps_1 * 1 *(1/(1+math.e**-int(packet_length)))
    probability += reps_0 * 2 *(1/(1+math.e**-int(packet_length)))
    rand = randint(1, 100)

    if rand <= probability:
        return True
    else:
        return False
