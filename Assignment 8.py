
with open("input.txt", "r") as file:
    lines = file.readlines()

    print("Total number of lines:", len(lines))

    first_two_lines = lines[:2]

with open("output.txt", "w") as file:
    file.writelines(first_two_lines)

print("First two lines written to output.txt")