
with open("file1.txt") as file:
    lines_1 = file.readlines()
    lines_1 = [line.rstrip() for line in lines_1]

with open("file2.txt") as file:
    lines_2 = file.readlines()
    lines_2 = [line.rstrip() for line in lines_2]


overlap = [number for number in lines_1 if number in lines_2]
print(overlap)
