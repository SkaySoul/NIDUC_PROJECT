from zaklocenia import *
from analiza import *
from generator import generate
import csv

size = input("długość sygnału: ")
ones_p = input("ilość jedynek(procentowo): ")
packet_size = input("długość pakietów: ")
number = input("liczba pomiarów na powtórzenie: ")
number_2 = input("liczba powtórzeń: ")
broken_packets = list()

file = open('results.csv', 'a')
writer = csv.writer(file)
header = ['(liczba pakietów poprawnych)  (liczba pakietów z błędami)  (procentowa ilość 1)  (rodzaj scramblera)']
writer.writerow(header)
file.close()

statistics = open('stats.csv', 'a')
writer2 = csv.writer(statistics)
header2 = ['(min) (first quartile) (median) (third quartile) (max) (average) (deviation)']
writer2.writerow(header2)


def negation():
    data = generate(size, ones_p, packet_size)
    # print(data)
    negationScramble(data)
    broken_packets.append(stats(data, packet_size, ones_p, "negation"))
    # print(data)
    negationDescramble(data)


def shift():
    data = generate(size, ones_p, packet_size)
    # print(data)
    shiftScramble(data, packet_size)
    broken_packets.append(stats(data, packet_size, ones_p, "shift"))
    # print(data)
    shiftDescramble(data, packet_size)


def multiplicative():
    data = generate(size, ones_p, packet_size)
    # print(data)
    multiplicativeScramble(data)
    broken_packets.append(stats(data, packet_size, ones_p, "multiplicative"))
    # print(data)
    multiplicativeDescramble(data)


def additive():
    data = generate(size, ones_p, packet_size)
    # print(data)
    additiveScramble(data)
    broken_packets.append(stats(data, packet_size, ones_p, "additive"))
    # print(data)
    additiveDescramble(data)


for x in range(0, int(number_2)):

    for i in range(0, int(number)):
        negation()

    for i in range(0, int(number)):
        shift()

    for i in range(0, int(number)):
        multiplicative()

    for i in range(0, int(number)):
        additive()

    writer2.writerow(
        [firstPointSummary(broken_packets), secondPointSummary(broken_packets), thirdPointSummary(broken_packets),
         fourthPointSummary(broken_packets), fifthPointSummary(broken_packets), arithmeticAverage(broken_packets),
         standardDeviation(broken_packets)])

    broken_packets.clear()

statistics.close()
