import random
from textwrap import indent


random_list : list[int] = []

even_index : list[int] = []
even_numbers : list[int] = []
inverted_list : list[int] = []
first_last : list[int] = []

for i in range(10):
    random_list.append(random.randint(1,100))

for number in random_list:
    #even index
    if (random_list.index(number)%2==0):
        even_index.append(number)
    #even numbers
    if (number %2 == 0):
        even_numbers.append(number)
    #inverted list
    inverted_list.insert(0,number)
    #first last
    if random_list.index(number) in (0,len(random_list)-1):
        first_last.append(number)
        
print(f"Random list : {random_list}")
print(f"Even index : {even_index}")
print(f"Even numbers : {even_numbers}")
print(f"Inverted list : {inverted_list}")
print(f"First last : {first_last}")