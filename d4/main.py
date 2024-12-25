input = []
with open("input.txt", "r") as file:
    input = [list(line.strip()) for line in file]


# Puzzle 1
# def find_match(map, x, y):
#     # Bounding box
#     T = 1 if ((y - 3) >= 0) else 0
#     B = 1 if ((y + 3) < len(map)) else 0
#     L = 1 if ((x - 3) >= 0) else 0
#     R = 1 if ((x + 3) < len(map[y])) else 0

#     t_word = "".join(map[y - i][x] for i in range(0,4)) if (T) else ""
#     b_word = "".join(map[y + i][x] for i in range(0,4)) if (B) else ""
#     l_word = "".join(map[y][x - i] for i in range(0,4)) if (L) else ""
#     r_word = "".join(map[y][x + i] for i in range(0,4)) if (R) else ""
#     tr_word = "".join(map[y - i][x + i] for i in range(0,4)) if (T and R) else ""
#     tl_word = "".join(map[y - i][x - i] for i in range(0,4)) if (T and L) else ""
#     br_word = "".join(map[y + i][x + i] for i in range(0,4)) if (B and R) else ""
#     bl_word = "".join(map[y + i][x - i] for i in range(0,4)) if (B and L) else ""

#     return (t_word == "XMAS") + (b_word == "XMAS") + (l_word == "XMAS") + (r_word == "XMAS") + (tr_word == "XMAS") + (tl_word == "XMAS") + (br_word == "XMAS") + (bl_word == "XMAS")


# count = 0
# for y in range(len(input)):
#     for x in range(len(input[y])):
#         count += find_match(input, x, y)

# print(count)


# Puzzle 2
def find_match(map, x, y):
    # Bounding box
    T = 1 if ((y - 1) >= 0) else 0
    B = 1 if ((y + 1) < len(map)) else 0
    L = 1 if ((x - 1) >= 0) else 0
    R = 1 if ((x + 1) < len(map[y])) else 0

    first = "".join(map[y+i][x+i] for i in range(-1, 2)) if (T and B and L and R) else ""
    second = "".join(map[y-i][x+i] for i in range(-1, 2)) if (T and B and L and R) else ""
    

    return ((first=="MAS" or first=="SAM") and (second=="SAM" or second=="MAS"))




count = 0
for y in range(len(input)):
    for x in range(len(input[y])):
        if(input[y][x] == "A"):
            count += find_match(input, x, y)

print(count)