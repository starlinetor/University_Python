classes = open("10.2.2_classes.txt", "r", encoding="utf-8")

classes_list : list[str] = []

while True:
    line = classes.readline().removesuffix("\n")
    if line == "" : 
        break
    
    classes_list.append(line)

classes.close()

student_id = input("Enter student id : ")

for class_uni in classes_list:
    #open class file
    class_uni_file = open(f"10.2.2_{class_uni}.txt", "r", encoding="utf-8")
    class_uni_list : list[list[str]] = []
    while True:
        line = class_uni_file.readline().removesuffix("\n")
        if line == "" : 
            break
        class_uni_list.append(line.split(" "))
    
    class_uni_file.close()
    
    for grade in class_uni_list:
        if student_id in grade:
            print(f"{class_uni} {grade[1]}")
        