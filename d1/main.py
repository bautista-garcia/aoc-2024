column1, column2 = [], []

# Open and read the file
with open('input.txt', 'r') as file:
    for line in file:
        # Split the line into two values
        value1, value2 = line.strip().split()
        # Append each value to the respective list
        column1.append(int(value1))  # Change to float(value1) if needed
        column2.append(int(value2))  # Change to float(value2) if needed


column1.sort()
column2.sort()

# Puzzle 1
distance = 0
for val1, val2 in zip(column1, column2):
    distance += abs(val1 - val2)

# Puzzle 2
sim1 = {}
sim2 = {}
for value1, value2 in zip(column1, column2):
    sim1[value1] = sim1.get(value1, 0) + 1
    sim2[value2] = sim2.get(value2, 0) + 1

similarity = 0
for key,value in sim1.items():
    similarity += value * (key * sim2.get(key, 0))


print(similarity)



        
        

