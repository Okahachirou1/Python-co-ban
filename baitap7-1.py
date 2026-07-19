import csv
files = {}
with open("logs/bills.csv", "r") as file:
    reader = csv.DictReader(file, skipinitialspace=True)
    for row in reader:
        if row["discount"] == "yes":
            date = row["datetime"].split()[0]
            filename = "report_" + date.replace("/", "-") + ".csv"
            total = int(row["billtotal"]) - int(row["discount_vnd"])
            if filename not in files:
                outfile = open(filename, "w", newline="")
                writer = csv.writer(outfile)
                writer.writerow(["id", "datetime", "total"])
                files[filename] = (outfile, writer)
            files[filename][1].writerow([
                row["id"],
                row["datetime"],
                total
            ])
for outfile, writer in files.values():
    outfile.close()
print("Hoàn thành!")