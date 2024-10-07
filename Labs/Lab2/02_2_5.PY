freshman_1: str = "s346716"
freshman_2: str = "s345543"

def freshman_number(freshman_code: str) -> int:
    return int(freshman_code[1:len(freshman_code)])

if(freshman_number(freshman_1)<freshman_number(freshman_2)):
    print(freshman_1)
    print(freshman_2)
else:
    print(freshman_2)
    print(freshman_1)

