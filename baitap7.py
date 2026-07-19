import csv
with open("logs/students.csv", "r") as file:
    reader = csv.DictReader(file, skipinitialspace=True)
    print("age\tincome\tbuyspc")
    for row in reader:
        if int(row["age"]) > 30:
            print(row["age"], row["income"], row["buyspc"], sep="\t")