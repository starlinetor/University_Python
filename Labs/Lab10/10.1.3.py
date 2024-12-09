from io import TextIOWrapper


files_str : str = input("Enter files : ")
word_to_find : str = input("Enter word : ")

files : list[str] = files_str.split(",")

lines : list[str] = []

for file in files:
    #open file
    in_file : TextIOWrapper = open(file, "r", encoding="utf-8")
    #get lines
    while True:
        line = in_file.readline()
        if line == "":
            break
        lines.append(line)

for line in lines:
    if line.lower().find(word_to_find) != -1:
        print(line.removesuffix("\n"))