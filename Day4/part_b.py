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
cards_dict = { e:1 for e in range(1, len(data) + 1) }
res = len(data)
for card in range(len(data)):
    while cards_dict[card + 1] >= 1:
        matchings = 0
        for c in data[card][1]:
            if c in data[card][0]:
                matchings += 1
                res += 1
        for i in range(card + 2, card + 2 + matchings):
            if i in range(len(data) + 1):
                cards_dict[i] += 1
        cards_dict[card + 1] -= 1

print(res)

