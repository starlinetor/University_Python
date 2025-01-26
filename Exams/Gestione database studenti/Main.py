def read_students() -> list[list[str]]:
    #open students file
    students_file : TextIOWrapper = open("studenti.csv", "r", encoding="utf-8")

    students_data : list[list[str,float]] = []

    for line in students_file:
        #save each line
        students_data.append(line.removesuffix("\n").split(","))

    #remove first line that is just info data
    students_data.remove(students_data[0])

    #close students file
    students_file.close()

    return students_data

def read_criteria() -> list[list[str]]:
    #open criteria file
    criteria_file : TextIOWrapper = open("criteria.txt", "r", encoding="utf-8")

    criteria_data : list[list[str]] = []

    #add first line

    for line in criteria_file:
        criteria_data.append(line.removesuffix("\n").split(","))

    #close criteria file
    criteria_file.close()

    return criteria_data

def print_student(student : list[str]) -> None:
    print("{" + f"'ID' : {student[0]}, 'cognome studente' : {student[1]}, 'grado' : {student[2]}, 'GPA' : {student[3]}"+"}")

def students_by_ID(ID : list[str], students_data : list[list[str]]) -> None: 
    print("Studenti trovati per ID:")
    for student in students_data:
        if student[0] in ID:
            #print data
            print_student(student)
    print()

def students_by_name(last_names : list[str], students_data : list[list[str]]) -> None: 
    for last_name in last_names:
        print("Studenti trovati per cognome:")
        for student in students_data:
            if student[1] == last_name:
                #print data
                print_student(student)
        print()

def gpa_avrage(grades : list[str], students_data : list[list[str]]) -> None: 
    for grade in grades:
        sum : float = 0
        students : int = 0
        for student in students_data:
            if student[2] == grade:
                #print data
                sum += float(student[3])
                students += 1
        if students == 0 :
            #prevents division by zero
            print(f"Grade : {grade} missing, skipped")
            continue
        print(f"Media del GPA per il grado {grade}: {sum/students:.2f}")

def main():
    students_data : list[list[str]] = read_students()
    criteria_data : list[list[str]] = read_criteria()

    #criteria data 0 is the id
    students_by_ID(criteria_data[0], students_data)
    #criteria data 1 is the name
    students_by_name(criteria_data[1], students_data)
    #criteria data 2 is the grade
    gpa_avrage(criteria_data[2], students_data)

if __name__ == "__main__":
    main()
