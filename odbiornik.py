from generator import generator

def receiver(file_name, package_size, data):

  file = open("packages.txt", "r")

  for data_index in range(0, len(data)):

    for index in range(0, package_size - 1):
      line = file.readline()
      popsute = 0
      niepopsute = 0

      if line[index] == data[data_index]:
        niepopsute += 1

      elif line[index] != data[data_index]:
        popsute += 1

  if (popsute + niepopsute) != 0:
    jak_bardzo_popsuty = popsute / (popsute + niepopsute)

  file.close()

