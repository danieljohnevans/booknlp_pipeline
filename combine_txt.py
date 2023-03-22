import os
import csv

directory = "output_dir"

rows = []

for subdir in os.listdir(directory):
    subdir_path = os.path.join(directory, subdir)
    if os.path.isdir(subdir_path):
        csv_file_path = os.path.join(subdir_path, subdir + ".entities")
        if os.path.exists(csv_file_path):
            with open(csv_file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter='\t')
                for row in reader:
                    row["book"] = subdir.split("|")[0]
                    row["page"] = subdir.split("|")[1]
                    rows.append(row)

with open("combined_entities.csv", "w", newline='') as csvfile:
    fieldnames = ["COREF", "start_token", "end_token", "prop", "cat", "text", "book", "page"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    for row in rows:
        writer.writerow(row)