import csv

data = csv.reader(open("labs.csv"))

concept = []
target = []

for i in data:
    concept.append(i[:-1])
    target.append(i[-1])

specific = ["0"] * len(concept[0])
general = [["?" for i in range(len(specific))] for i in range(len(specific))]

for i, instance in enumerate(concept):
    if target[i] == "Yes":
        for x in range(len(specific)):
            if specific[x] == "0":
                specific[x] = instance[x]
            elif instance[x] != specific[x]:
                specific[x] = "?"
                general[x][x] = "?"
    else:
        for x in range(len(specific)):
            if specific[x] != instance[x]:
                general[x][x] = specific[x]
            else:
                general[x][x] = "?"

indices = [i for i,val in enumerate(general) if val == ["?" for i in range(len(specific))]]

for i in indices:
    general.remove(["?" for i in range(len(specific))])

print(specific)
print(general)
