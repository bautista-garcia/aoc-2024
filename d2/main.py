# # Read input
# rows = []
# with open('input.txt', 'r') as file:
#     for line in file:
#         rows.append([int(num) for num in line.strip().split()])


# Puzzle 1
# s = 0
# safe = 0
# for i in range(len(rows)):
#     for j in range(len(rows[i]) - 1):
#         # Compute distance
#         dist = rows[i][j] - rows[i][j + 1]

#         # Compute inc or dec
#         if(j == 0): s = dist

#         # Check safety
#         if ((abs(dist) < 1) or (abs(dist) > 3) or ((s * dist) < 0)):
#             break
#         elif (j == (len(rows[i]) - 2)):
#             safe += 1
        

# Puzzle 2
def check_state(n1, n2):
    d = n2 - n1
    if (abs(d) > 3 or abs(d) < 1): state = 0
    else: state = 1 if (d > 0) else -1

    return state


invalid = []

rows = [[1, 2, 3, 4, 5], [1, 1, 1, 2, 4, 5], [25, 26, 20, 23]]

for i in range(len(rows)):
    state = check_state(rows[i][0], rows[i][1])
    invalid_count = 0 if (state != 0) else 1
    prev = rows[i][0]
    print(f"Lista {i}")
    # print(f"State {state}, input {state}")
    for j in range(1, len(rows[i]) - 1):
        input = check_state(rows[i][j], rows[i][j + 1])
        print(f'State {state}, input {input}')
        if (state == 0):
            if((input == 0)):
                invalid_count += 1
                print(f"Suma en j: {j}")
        elif ((state * input) == (-1)):
            invalid_count += 1
            print(f"Suma en j:{j}")
        else: state = input
        prev = rows[i][j]

    if (invalid_count > 1): invalid.append(rows[i])


print(len(invalid))




