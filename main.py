from zaklocenia import *
from analiza import stats
from generator import generate

size = input("długość sygnału: ")
ones_p = input("ilość jedynek(procentowo): ")
packet_size = input("długość pakietów: ")

data = generate(size, ones_p, packet_size)

print(data)
# save(packet_size, data)

# negationScramble(data)
# print(data)
# negationDescramble(data)

# shiftScramble(data, packet_size)
# print(data)
# shiftDescramble(data, packet_size)

multiplicativeScramble(data)
print(data)
multiplicativeDescramble(data)

# additiveScramble(data)
# print(data)
# additiveDescramble(data)

# save(packet_size, data)

# repeatCounter(data, packet_size)

print(data)

stats(data, packet_size, ones_p)
