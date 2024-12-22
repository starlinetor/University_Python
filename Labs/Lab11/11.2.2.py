from io import TextIOWrapper
from tracemalloc import start

#open and read file
infile : TextIOWrapper = open("11.2.2_codice_genetico.csv", "r", encoding="utf-8")

infile_list = infile.readlines()

infile.close()

amminoacids : dict[str : str] = {}
instruction : dict[str : str] = {} 

for line in infile_list:
    line_list = line.split(",")
    #clean lines from junk
    for i in range(len(line_list)):
        line_list[i] = line_list[i].strip("\n").strip("\"").strip()
        
    #save instruction dna
    if line_list[0] == "stop" or line_list[0] == "start":
        for i in range(1,len(line_list)):
            instruction[line_list[i]] = line_list[0]
    else:
        for i in range(1,len(line_list)):
            amminoacids[line_list[i]] = line_list[0]

genome = "GUAUGCACGUGACUUUCCUCAUGAGCUGAU"

starting_index : int = -1

for i in range(len(genome)):
    code = genome[i:i+3]
    if instruction.get(code,"") == "start":
        starting_index = i
        break

if(starting_index == -1):
    print("Missing starting sequence")
    exit()

genome_list = []
ending_sequence : bool = False

for i in range(starting_index, len(genome), +3):
    code = genome[i:i+3]
    if instruction.get(code,"") == "stop":
        genome_list.append("stop")
        ending_sequence = True
        break
    genome_list.append(amminoacids[code])

if ending_sequence == False:
    print("Missing ending sequence")
    exit()

print("".join(genome_list))