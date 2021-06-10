from generator import generate

size = input("długość sygnału: ")
ones_p = input("ilość jedynek(procentowo): ")
packet_size = input("długość pakietów: ")

generate(size, ones_p, packet_size)
