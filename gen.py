import csv
import pandas as pd
file_name = "airtravel.csv"
# df = pd.read_csv(file_name)
# print(pd.options.display.max_rows)
# print(df.to_string())

# with open(file_name, 'r') as f:          # Read lines separately
#     reader = csv.reader(f, delimiter='t')
#     for i, line in enumerate(reader):
#         print(i, line)


def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row


# csv_gen = (row for row in open(file_name))
g = csv_reader(file_name)
print(next(g))
print(next(g))
print(next(g))
# csv_gen = csv.csv_reader("airtravel.csv")
# row_count = 0

# for row in csv_gen:
#     row_count += 1

# print(f"Row count is {row_count}")
