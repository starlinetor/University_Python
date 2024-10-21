numbers : list[int] = []

while True:
    numbers.append(int(input("Enter a new number: ")))

    odd: int = 0
    even: int = 0

    for number in numbers:
        if number%2==0:
            even += 1
        else:
            odd += 1

    print  (f"The total is : {sum(numbers)} \n"
            f"The max value is {max(numbers)}, the min value is {min(numbers)} \n"
            f"The odd numbers are {odd}, the even numbers are {even}\n") 