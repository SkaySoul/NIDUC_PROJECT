import csv
import numpy as np
from odbiornik import packetDetector
import matplotlib.pyplot as plt
import scipy.stats as st

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


def firstPointSummary(brokenPackets):
    return np.percentile(brokenPackets, 0, interpolation='midpoint')


def secondPointSummary(brokenPackets):
    return np.percentile(brokenPackets, 25, interpolation='midpoint')


def thirdPointSummary(brokenPackets):
    return np.percentile(brokenPackets, 50, interpolation='midpoint')


def fourthPointSummary(brokenPackets):
    return np.percentile(brokenPackets, 75, interpolation='midpoint')


def fifthPointSummary(brokenPackets):
    return np.percentile(brokenPackets, 100, interpolation='midpoint')


def arithmeticAverage(brokenPackets):
    return np.mean(brokenPackets)


def standardDeviation(brokenPackets):
    return round(np.std(brokenPackets), 3)


"""def analyze(brokenPackets):
  analyzed = fivePointSummary(brokenPackets)
  fig = plt.boxplot(brokenPackets)
  fig.savefig('wykres_pudelkowy.svg')
  fig1, axs = plt.subplots(1, 2)
  n_bins = len(brokenPackets)
  axs[0].hist(brokenPackets['Histogram'], bins=n_bins)
  fig1.savefig('histogram.svg')
"""
 
def plots(brokenPackets):
  fig, axes = plt.subplots(1, 2, figsize=(12, 4))
  
  n_bins = len(brokenPackets)
  axes[0].hist(brokenPackets, bins=n_bins, density = 'true', label = "Data")
  axes[0].set(title = 'Histogram')
  axes[0].set(xlabel = 'Data')
  axes[0].set(ylabel = 'Frequirency')
  axes[0].legend(loc="upper right")
 
  axes[1].boxplot(brokenPackets)
  axes[1].set(title = 'Boxplot')
  axes[1].set(xlabel = 'Data')
  axes[1].set(ylabel = 'Frequirency')
  

  plt.savefig('plot.svg')
  plt.show()



  


