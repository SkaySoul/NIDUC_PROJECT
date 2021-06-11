import csv
from numpy import np
from odbiornik import packetDetector


# analiza etap 2- https://datko.pl/NiDUC2/etap2.pdf
# TODO poprawić csv(dostosować do analizy), ANALIZA!!!


# zapis pomiarów do pliku csv
def stats(data, packet_length, one, scr_type):
    file = open('results.csv', 'a')
    writer = csv.writer(file)
    broken = int(packetDetector(data, packet_length))
    good = int((len(data) / int(packet_length)) - broken)
    writer.writerow([good, broken, one, scr_type])
    file.close()
    return broken



def fivePointSummary(data):
  return np.percentile(data, [0, 25, 50, 75, 100], interpolation='midpoint')
  

def analyze(data):
  analyzed = fivePointSummary(data)
  iqr = analyzed[3]-analyzed[1]
  
