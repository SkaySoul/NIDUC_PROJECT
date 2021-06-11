from zaklocenia import *
from analiza import stats
from generator import generate
import csv

size = input("długość sygnału: ")
ones_p = input("ilość jedynek(procentowo): ")
packet_size = input("długość pakietów: ")
option = input("1-neg 2-shift 3-mult 4-add")
number = input("liczba powtórzeń")
broken_packets = list()

file = open('results.csv', 'a')
writer = csv.writer(file)
header = ['(liczba pakietów poprawnych)  (liczba pakietów z błędami)  (procentowa ilość 1)  (rodzaj scramblera)']
writer.writerow(header)
file.close()

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

