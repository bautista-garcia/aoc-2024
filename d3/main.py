import re

memory = ""
with open('input.txt', 'r') as file:
    memory = file.read()

# # Puzzle 1
# pattern = r"mul\((\d+),(\d+)\)"
# matches = re.findall(pattern, memory)

# # Print results
# sum = 0
# for x1, x2 in matches:
#     sum += (int(x1) * int(x2))

# print(sum)


# Puzzle 2
ena = r"(do\(\))|(don't\(\))"
substrings = re.split(ena, memory)

sum = 0
flag = 1
pattern = r"mul\((\d+),(\d+)\)"
for text in substrings:
    if(flag and (text != None)):
        matches = re.findall(pattern, text)
        for x1, x2 in matches:
            sum += (int(x1) * int(x2))

    if(text == "do()"): flag = 1
    elif(text == "don't()"): flag = 0

print(sum)