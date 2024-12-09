from io import TextIOWrapper
import random
from sqlite3 import DataError

def gen_file():
    
    name_list = ["Nino", "Gino", "Armando", "Bob", "Tino", "Ciro", "Lello", "Giacinto", "Peppino", "Franco"]
    surname_list = ["Bizzarro", "Colibrì", "Zucchero", "Frullino", "Galletto", "Scozzese", "Barbuto", "Lombrico", "Ventoso", "Sghembo"]
    services_list = ["Repair", "Delivery", "Customization", "Consultation", "Installation"]
    
    out_file : TextIOWrapper = open("10.1.4_sells_log.txt", "w", encoding="utf-8")
    for _ in range(10):
        out_file.write( f"{name_list[random.randint(0,9)]} {surname_list[random.randint(0,9)]};"
                        f"{services_list[random.randint(0,4)]};"
                        f"{random.random()*100:.2f};"
                        f"{random.randrange(1,28)}/{random.randrange(1,12)}/2024\n"
                        )

def check_format(file : list[list[str]]):
    for line in file :
        #Name 
        if len(line) != 4:
            raise DataError("Wrong file format, each line should have 4 values divided by ;")
        #price must be a float
        try:
            float(line[2])
        except:
            raise DataError("Wrong file format, each price should be a float")
        #date
        date = line[3].split("/")
        if len(date) != 3:
            raise DataError("Wrong file format, each date should have 3 values divided by ;")
        for value in date:
            try:
                int(value)
            except:
                raise DataError("The date should be made only by integers")
        
#gen_file()

in_file = open("10.1.4_sells_log.txt", "r", encoding="utf-8")

lines : list[list[str]] = []

while True:
    line = in_file.readline().removesuffix("\n")
    if line == "":
        break
    lines.append(line.split(";"))

in_file.close()

check_format(lines)

services : dict[str:float] = {}

for line in lines:
    if line[1] not in services.keys():
        services[line[1]] = float(line[2])
    else:
        services[line[1]] += float(line[2]) 

print(services)