
LETTERS: list = ["j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
NUMS = [str(x) for x in list(range(0, 10))]

starting_point = "3e"

print(starting_point[1].lower() in LETTERS)
print(NUMS)
print((starting_point[0]) in NUMS)

if (starting_point[1].lower() in LETTERS) and (int(starting_point[0]) in NUMS):
    print(starting_point[1].lower() in LETTERS)
    print(int(starting_point[0]) in NUMS)