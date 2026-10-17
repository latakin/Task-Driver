import csv

def savefile(tasklist,filename):
    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, fieldnames= ["creator", "request", "priority","date", "status"])
        writer.writeheader()
        writer.writerows(tasklist)



def getfile(filename, tasklist):
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasklist.append({"creator": row["creator"], "request": row["request"], "priority": row["priority"], "date": row["date"], "status": row["status"]})
    except FileNotFoundError:
        print("File doesnt exist yet")