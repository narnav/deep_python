import csv
import numpy as np


def getData(filename1):
    with open(filename1, "r") as csv1:
        reader1 = csv.reader(csv1)
        for row1 in zip(reader1):
            yield (np.array(row1))


for tup in getData("airtravel.csv"):
    print(tup)
