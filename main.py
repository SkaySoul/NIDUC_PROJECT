from generator import generator
from zaklocenia import negationScramble, negationDescramble
from zaklocenia import shiftScramble, shiftDescramble
from zaklocenia import multiplicativeScramble, multiplicativeDescramble
from zaklocenia import additiveScramble, additiveDescramble
from analiza import repeatCounter, stats

size = input("długość sygnału: ")
ones_p = input("ilość jedynek(procentowo): ")
packet_size = input("długość pakietów: ")

data = generator(size, ones_p, packet_size)

print(data)
# save(packet_size, data)

# negationScramble(data)
# print(data)
# negationDescramble(data)

#shiftScramble(data, packet_size)
#print(data)
#shiftDescramble(data, packet_size)

multiplicativeScramble(data)
print(data)
multiplicativeDescramble(data)

# additiveScramble(data)
# print(data)
# additiveDescramble(data)

# save(packet_size, data)

# repeatCounter(data, packet_size)

print(data)

stats(data, packet_size)
