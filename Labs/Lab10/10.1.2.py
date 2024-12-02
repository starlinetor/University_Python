#open files
in_file = open("10.1.2_input.txt", "r", encoding="utf-8")
out_file = open("10.1.2_output.txt", "w", encoding="utf-8")

lines : list[str] = []
#read the out_file
while True:
    line = in_file.readline()
    if line == "":
        #the last line of every file is always empty
        #an empty line is "\n"
        break
    lines.append(line)

#print to file backwards
for i in range(len(lines)-1,-1,-1):
    if i == len(lines)-1:
        #the last line is missing the \n so we have to add it ourselves
        out_file.write(f"{lines[i]}\n")
    else :
        out_file.write(f"{lines[i]}")

#close the files
in_file.close()
in_file.close()