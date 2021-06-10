import csv
from odbiornik import packetDetector


# analiza etap 2- https://datko.pl/NiDUC2/etap2.pdf
# TODO poprawić csv(dostosować do analizy), ANALIZA!!!


# zapis pomiarów do pliku csv
def stats(data, packet_length):
    file = open('results.csv', 'w')
    writer = csv.writer(file)
    header = ['(długość pakietów)  (procentowa ilość 1)  (ilość popsutych pakietów)  (rodzaj scramblera)']
    writer.writerow(header)
    writer.writerow([packet_length, packetDetector(data, packet_length)])
    file.close()
