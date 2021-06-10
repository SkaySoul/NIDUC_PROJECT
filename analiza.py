# TODO analiza etap 2- https://datko.pl/NiDUC2/etap2.pdf
# poprawić csv(dostosować do analizy), poprawa struktury projektu, analiza, poprawa funkcji wyznaczającej prawdopodobieństwo zepsucia
from random import randint
import csv


def repeatCounter(data, packet_length):
    reps_0_max = 0
    reps_0 = 0
    reps_1_max = 0
    reps_1 = 0
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
                
            if index == (int(packet_length)-1):
                if reps_1_max < reps_1:
                    reps_1_max = reps_1
                if reps_0_max < reps_0:
                    reps_0_max = reps_0
              
        if probabilityOfCorruption(reps_1_max, reps_0_max, packet_length):
          bad_packets += 1
        else:
          good_packets += 1
        temp += int(packet_length)

    return bad_packets
        

def probabilityOfCorruption(reps_1, reps_0, packet_length):
  probability = 0
  probability += reps_1 * 2
  probability += reps_0 * 3
  #probability /= packet_length
  rand = randint(1, 100)

  if rand <= probability:
    return True
  else:
    return False


def stats(data, packet_length):
  file = open('results.csv', 'w') 
  writer = csv.writer(file)
  header = ['liczba popsutych pakietów']
  writer.writerow(header)
  writer.writerow([repeatCounter(data, packet_length)])
  file.close()



  

# długość pakietów, procentowa ilość 1, ilość pakietów popsutych, rodzaj scramblera