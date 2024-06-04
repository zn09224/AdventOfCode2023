def input(filename):
    with open(filename) as f:
        lines = f.readlines()
    data = []
    for line in lines:
        line = line[9:]
        line = line.strip()
        a, b = line.split('|')
        a = a.strip()
        b = b.strip()
        set1 = {int(q) for q in a.split()}
        set2 = {int(q) for q in b.split()}
        data.append([set1, set2])  
    return data

data = input("input_4.txt")

res = 0
for card in data:
    points = 0
    for c in card[1]:
        if c in card[0]:
            if points == 0:
                points = 1
            else:
                points = points * 2
    res += points

print(res)

