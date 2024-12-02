input_file = open("10.1.1_input.txt", "r", encoding="utf-8")
output_file = open("10.1.1_output.txt", "w", encoding="utf-8")


lines : list[str] = []

for line in input_file:
    lines.append(line)

for i in range(len(lines)):
    output_file.write(f"/*{i+1}*/{lines[i]}")

#end code
input_file.close()
output_file.close()