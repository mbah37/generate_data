from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

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
    current_date = datetime.strptime(row[0], "%Y-%m-%d")
    rates = float(row[1])
    dates.append(current_date)
    ur_rates.append(rates)

plt.style.use('dark_background')
figure, graph = plt.subplots()

graph.plot(dates, ur_rates)
graph.set_title("Unemployment Rate by Month(OH) 1976-2022", fontsize=20)
graph.set_ylabel("Unemployment Rate (%)", fontsize=14)
figure.autofmt_xdate()

plt.show()