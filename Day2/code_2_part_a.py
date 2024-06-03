def input(filename):
    with open(filename) as f:
        lines = f.readlines()

    games = {}

    for line in lines:
        line = line.strip()
        if line.startswith("Game"):
            parts = line.split(": ")
            game_number = int(parts[0].split()[1])
            games[game_number] = []
            counts = parts[1].split("; ")
            for count in counts:
                color_dict = {}
                color_counts = count.split(", ")
                for color_count in color_counts:
                    value, color = color_count.split()
                    color_dict[color] = int(value)
                games[game_number].append(color_dict)

    return games

data = input("input_2.txt")

def prob(data):
    r = "red"
    g = "green"
    b = "blue"
    res = 0

    for game in data.keys():
        flag = True
        for turn in data[game]:
            if r in turn and turn[r] > 12:
                flag = False
                break
            if g in turn and turn[g] > 13:
                flag = False
                break
            if b in turn and turn[b] > 14:
                flag = False
                break
        if flag == True:
            res += game
    return res

print(prob(data))

      
        
