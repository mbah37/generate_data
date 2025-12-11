from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Create a Path object pointing to the CSV file containing Ohio unemployment data.
path = Path('OHUR (1).csv')

# Read the contents of the CSV file as text, split into individual lines.
lines = path.read_text(encoding='utf-8').splitlines()

# Create a CSV reader from the lines.
reader = csv.reader(lines)

# Read the first line of the file, which contains the header row.
header = next(reader)
# print(header)

# Optional code for printing header structure:
# for index, column_title in enumerate(header):
#     print(f"{index} {column_title}, ", end= " ")
# print()

# Lists to store dates and unemployment rates from the CSV file.
dates = []
ur_rates = []

# Loop through each row in the CSV and extract its values.
for row in reader:
    # Convert date string (YYYY-MM-DD) into a datetime object.
    current_date = datetime.strptime(row[0], "%Y-%m-%d")
    rates = float(row[1])

    # Append data into lists.
    dates.append(current_date)
    ur_rates.append(rates)

#dark background style for the graph.
plt.style.use('dark_background')

figure, graph = plt.subplots()

# Plot unemployment rates over time.
graph.plot(dates, ur_rates, color='blue', linewidth=2, linestyle='dashed')

# Add main chart title and axis labels.
graph.set_title("Unemployment Rate by Month(OH) 1976-2022", fontsize=20)
graph.set_ylabel("Unemployment Rate (%)", fontsize=14)
graph.set_xlabel("Dates", fontsize=14)

# Automatically rotate and align date labels for readability.
figure.autofmt_xdate()

plt.show()