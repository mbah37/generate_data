from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('OHUR (1).csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header = next(reader)
#print(header)

