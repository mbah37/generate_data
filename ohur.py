from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('OHUR (1).csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header = next(reader)
#print(header)

for index, column_title in enumerate(header):
    print(f"{index} {column_title}, ", end= " ")
print()

dates = []
ur_rate = []

for row in reader:
    rates = int(row[1])
    ur_rate.append(rates)