from generator import generator

size = input("długość sygnału: ")
ones_p = input("ilość jedynek(procentowo): ")
packet_size = input("długość pakietów: ")

generator(size, ones_p, packet_size)
