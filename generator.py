from random import shuffle
from zaklocenia import negationScrambler
from zaklocenia import repeatScrambler
from zaklocenia import cezarScramble

def generator(size, ones_p, packet_size):

  zeros = int(size) - round(int(size) * int(ones_p)/100,0)
  ones=int(size)-int(zeros)

  data = [0]*int(zeros) + [1]*int(ones)
  shuffle(data)
  print (data)
  #save(packet_size, data)
  #negationScrambler(data)
  #print(data)
  #repeatScrambler(data)
  cezarScramble(data, packet_size)
  save(packet_size, data)
  print(data)



def save(packet_size, data):
  file = open("packages.txt", "w+")   # "w+"- do zapisu i odczytu

  for index in range(1, len(data)+1):
    file.write(str(data[index-1]))
    if index % int(packet_size) == 0:
     file.write("\n")

  file.close() 


