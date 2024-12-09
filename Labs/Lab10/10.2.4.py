from io import TextIOWrapper

infile : TextIOWrapper = open("10.2.4_bond_data.txt", "r", encoding="utf-8")

lines : list[list[str]] = []

while True:
    line = infile.readline()
    if line == "":
        break
    
    lines.append(line.removesuffix("\n").split(" "))

parameter = input()

for line in lines:
    if parameter in line:
        for value in line:
            if value != parameter:
                print(value, end=", ")
        print()