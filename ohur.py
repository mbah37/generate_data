from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('OHUR (1).csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header = next(reader)
#print(header)

#for index, column_title in enumerate(header):
    #print(f"{index} {column_title}, ", end= " ")
#print()

dates = []
ur_rates = []

for row in reader:
    rates = float(row[1])
    ur_rates.append(rates)

plt.style.use('dark_background')
figure, graph = plt.subplots()

graph.plot(ur_rates)
graph.set_title("Unemployment Rate by Month(OH) 1976-2022", fontsize=20)

plt.show()