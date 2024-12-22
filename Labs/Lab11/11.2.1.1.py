from io import TextIOWrapper

#open close file
infile : TextIOWrapper = open("11.2.1.1_rawdata_2004.txt", "r", encoding="utf-8")

infile_list = infile.readlines()

infile.close()

#exctract data
data : dict[str:int] = {}

for line in infile_list:
    #split the data
    line_list = line.split("$")
    #remove junk from the name of the country
    line_list[0] = line_list[0].split("\t")[1]
    #remove junk from the ernings
    line_list[1] = line_list[1].lstrip().removesuffix("\n")
    
    data[line_list[0]] = line_list[1]

while True:
    command = input("Enter a country or type quit to exit : ")
    if command == "quit":
        exit()
    if command in data.keys():
        print(f"{command} : {data[command]}$")
    else:
        print("Invalid command or country")