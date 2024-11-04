from roman import roman
import importlib.util 
    
spec = importlib.util.spec_from_file_location(
    name="roman_converter",  
    location=r"C:\Users\edora\OneDrive\Documenti\GitHub\University_Python\Labs\Lab6\06.2.2.py",
)
roman_converter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(roman_converter)

valid_numbers = 0
correct_numbers = 0

test_lenght: int = 8000

debug_print : bool = True

for i in range(1,test_lenght+1):
    
    if(roman_converter.valid_roman(str(roman(i).encode("ascii")))):
        valid_numbers +=1
    elif debug_print : 
        print(i, roman(i),"\n")
    if(i == roman_converter.convert_roman(str(roman(i).encode("ascii")))):
        correct_numbers += 1
    elif debug_print : 
        print(i, roman(i), "\n")
        
print(f"valid numbers percentage {round(valid_numbers/test_lenght * 100,2)}%")
print(f"correct numbers percentage {round(correct_numbers/test_lenght * 100,2)}%")

#note the code is able to convert back to decimal every number even above 4000 aka MMMM
#But it will mark them as wrong written numbers following the max of 3 repetition for each character