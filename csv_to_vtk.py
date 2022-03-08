import csv
import numpy as np
from pyevtk.hl import pointsToVTK

path_to_csv = "cube_centers_overlap.csv"

x = []
y = []
z = []
overlap = []

with open(path_to_csv, newline = '') as csvfile:
    filereader = csv.reader(csvfile, delimiter = ',')

    for row in filereader:
        x.append(row[0])
        y.append(row[1])
        z.append(row[2])
        overlap.append(row[3])



x = np.float64(x)
y = np.float64(y)
z = np.float64(z)
overlap = np.float64(overlap)

pointsToVTK("./visualization", x, y, z, data = {"overlap": overlap})