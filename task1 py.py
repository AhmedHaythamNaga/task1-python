import csv


try:
  result = open("result.csv", "x", newline="")
except FileExistsError:
  print("error")
  exit()

with open("result.csv", "w", newline="") as csvfile:
 result = csv.writer(csvfile)
 for i in range(2, 6):
        for j in range(1, 13):
            z = i * j
            result.writerow([i, " * ", j, " ", z])
        else:result.writerow([" "])

