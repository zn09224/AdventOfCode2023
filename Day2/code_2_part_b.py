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
        max_r = 0
        max_g = 0
        max_b = 0
        for turn in data[game]:
            if r in turn and turn[r] > max_r:
                max_r = turn[r]
            if g in turn and turn[g] > max_g:
                max_g = turn[g]
            if b in turn and turn[b] > max_b:
                max_b = turn[b]
        res += (max_r * max_g * max_b)
    return res

print(prob(data))

      
        
