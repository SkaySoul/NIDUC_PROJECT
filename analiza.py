import csv
from odbiornik import packetDetector


# analiza etap 2- https://datko.pl/NiDUC2/etap2.pdf
# TODO poprawić csv(dostosować do analizy), ANALIZA!!!


# zapis pomiarów do pliku csv
def stats(data, packet_length, one):
    file = open('results.csv', 'w')
    writer = csv.writer(file)
    header = ['(liczba pakietów poprawnych)  (liczba pakietów z błędami)  (procentowa ilość 1)  (rodzaj scramblera)']
    writer.writerow(header)
    broken = int(packetDetector(data, packet_length))
    good = int((len(data) / int(packet_length)) - broken)
    writer.writerow([good, broken, one, 'Multiplicative'])
    file.close()
