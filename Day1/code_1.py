def input(filename):
    with open(filename) as f:
        lines = f.readlines()
    data = []
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        characters = list(line)  # Convert line to list of characters
        data.append(characters)  # Add list of characters to the main list
    return data

data = input("input.txt")


def result(data):
    nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    res = 0
    for l in data:
        left = 0
        right = len(l) - 1
        while not l[left].isdigit() or not l[right].isdigit():
            if (left + 3) <= len(l) and not l[left].isdigit():
                s = ''.join(l[left:left + 3])
                if s in nums:
                    l[left] = str(nums[s])  
            if (left + 4) <= len(l) and not l[left].isdigit():
                s = ''.join(l[left:left + 4])
                if s in nums:
                    l[left] = str(nums[s])
            if (left + 5) <= len(l) and not l[left].isdigit():
                s = ''.join(l[left:left + 5])
                if s in nums:
                    l[left] = str(nums[s])
            if (left + 6) <= len(l) and not l[left].isdigit():
                s = ''.join(l[left:left + 6])
                if s in nums:
                    l[left] = str(nums[s])
            if (right - 2) >= 0 and not l[right].isdigit():
                s = ''.join(l[right - 2:right + 1])
                if s in nums:
                    l[right] = str(nums[s])
            if (right - 3) >= 0 and not l[right].isdigit():
                s = ''.join(l[right - 3:right + 1])
                if s in nums:
                    l[right] = str(nums[s])
            if (right - 4) >= 0 and not l[right].isdigit():
                s = ''.join(l[right - 4:right + 1])
                if s in nums:
                    l[right] = str(nums[s])
            if (right - 5) >= 0 and not l[right].isdigit():
                s = ''.join(l[right - 5:right + 1])
                if s in nums:
                    l[right] = str(nums[s])
            if not l[left].isdigit():
                left += 1
            if not l[right].isdigit():
                right -= 1
        res += (int(l[left])*10) + int(l[right])
    
    return res

print(result(data))