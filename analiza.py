# TODO  Zliczyć ile w pakiecie występuje niezmiennych sekwencji różnej długości np. w pakiecie 100111  mamy 0*2 i 1*3 i w zależnośći od wystąpień przy sobie zwiększamy prawdopodobieństwo zepsucia pakietu
# TODO losujemy prawdopodobieństwo czy pakiet jest popsuty


def repeatCounter(data, packet_length):
    reps_0_max = 0
    reps_0 = 0
    reps_1_max = 0
    reps_1 = 0

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
                
            if index == (int(packet_length)-1):
                if reps_1_max < reps_1:
                    reps_1_max = reps_1
                if reps_0_max < reps_0:
                    reps_0_max = reps_0
              
        print("Jedynki: " + str(reps_1_max))
        print("Zera: " + str(reps_0_max))
        temp += int(packet_length)
        

