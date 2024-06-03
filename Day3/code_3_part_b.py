def input(filename):
    with open(filename) as f:
        lines = f.readlines()
    data = []
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        characters = list(line)  # Convert line to list of characters
        data.append(characters)  # Add list of characters to the main list
    return data
data = input("input_3.txt")
rows = len(data)
cols = len(data[0])
curr = ""
flag = False
sum = 0
d = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
for i in range(rows):
    for j in range(cols):
        if not data[i][j].isdigit() and curr != "":
            if flag == True:
                sum += int(curr)
            flag = False
            curr = ""
        elif data[i][j].isdigit():
            if flag == False:
                for dy, dx in d:
                    y, x = i + dy, j + dx
                    if (y in range(rows)
                        and x in range(cols) and
                        data[y][x] != "." and
                        data[y][x].isdigit() == False):
                        flag = True
            curr = curr + data[i][j]
    if curr != "" and flag == True:
        sum += int(curr)
        flag = False
        curr = ""
print(sum)
                
            
            
