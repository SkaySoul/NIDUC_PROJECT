def negation(data):
    index = 0
    while(index < len(data)):
      if(data[index] == 0):
        data[index] = 1
      elif(data[index] == 1):
        data[index] = 0
      index += 2  
      