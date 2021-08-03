import csv


with open('school_task.csv') as csvfile:
    data = csv.reader(csvfile, delimiter = ',')
    n = 0
    for row in data:
        print(', '.join(map(lambda x: str(x).strip(), row)))
        n += 1
    print(f"Number of rows in the list: {n}")
