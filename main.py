import numpy as np
import csv

# --------------------------------------------------M15--------------------------------------------------
M15_file = csv.reader(open("AUDUSD_M15_2019_2022(10_10).csv"))

M15_open = []
M15_high = []
M15_low = []
M15_close = []

for row in M15_file:
    M15_open.append(row[2])
    M15_high.append(row[3])
    M15_low.append(row[4])
    M15_close.append(row[5])


M15_open = np.array(M15_open)
M15_high = np.array(M15_high)
M15_low = np.array(M15_low)
M15_close = np.array(M15_close)
