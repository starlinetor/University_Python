male_exceptions: tuple[str] = ("belize", "cambodge", "mexique", "mozambique", "zaïre", "zimbabwe")
plural: tuple[str] = ("etats-unis", "pays-bas")
vocals: tuple[str] = ('a', 'e', 'i', 'o', 'u') 
adjective : str = ""

name_input = input("Enter the name of a country in french ")
#i decided to lower the name so capitalizatiomn is not relevant -> Belize == belize
name = name_input.lower()

#male or female
if (name[len(name)-1] == 'e'):
    #female
    adjective = "la"
else:
    #male
    adjective = "le"

#names starting with a vocal
if(name[0] in vocals):
    adjective = "l'"
    
#exceptions
if(name in male_exceptions):
    adjective = "le"

if(name in plural):
    adjective = "les"
    
print(f"{adjective} {name_input}")