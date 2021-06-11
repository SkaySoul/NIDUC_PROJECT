from zaklocenia import *
from analiza import *
from generator import generate
import csv

size = input("długość sygnału: ")
ones_p = input("ilość jedynek(procentowo): ")
packet_size = input("długość pakietów: ")
<<<<<<< HEAD
number = input("liczba pomiarów na powtórzenie: ")
number_2 = input("liczba powtórzeń: ")
=======
option = input("1-neg 2-shift 3-mult 4-add")
number = input("liczba powtórzeń")
>>>>>>> 6e563e8eda5b0e2d868cac4fd3980d921e8e4367
broken_packets = list()

file = open('results.csv', 'a')
writer = csv.writer(file)
header = ['(liczba pakietów poprawnych)  (liczba pakietów z błędami)  (procentowa ilość 1)  (rodzaj scramblera)']
writer.writerow(header)
file.close()

<<<<<<< HEAD
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

  writer2.writerow([firstPointSummary(broken_packets), secondPointSummary(broken_packets), thirdPointSummary(broken_packets), fourthPointSummary(broken_packets), fifthPointSummary(broken_packets), arithmeticAverage(broken_packets), stendardDeviation(broken_packets)])
  #tutaj robimy coś z listą -> statystyka 5-punktowa
  broken_packets.clear()

statistics.close()
=======
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
 

switcher = {
    1: negation,
    2: shift,
    3: multiplicative,
    4: additive
    }


for i in range(0, number):
  switcher[option]


broken_packets.clear()

>>>>>>> 6e563e8eda5b0e2d868cac4fd3980d921e8e4367
