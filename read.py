import csv

with open("bs.csv", "r") as file:
    lector_csv = csv.reader(file)
    lines_csv = list(lector_csv)
    for i in lines_csv:
        if i[0] == "14/12/2023":
            for n, j in enumerate(i):
                if n <= 1:
                    print(j)
                else:
                    print(str(lines_csv[0][n] + ": " + j) + " Bs.")
                if n == 8:
                    print("\n")
                