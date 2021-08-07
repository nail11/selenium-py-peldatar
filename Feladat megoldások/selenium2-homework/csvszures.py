import csv

with open('table_in.csv') as csv_file:
    file_content = csv.DictReader(csv_file)
    with open("table_out.csv", mode="w", newline='') as csv_file2:
        field_names = ['Email', 'Name']
        writer = csv.DictWriter(csv_file2, fieldnames=field_names)
        writer.writeheader()
        for row in file_content:
            writer.writerow({'Email': str(row['Email']).strip(), 'Name':str(row['Name']).strip()})