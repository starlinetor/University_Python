def subsidy_calculator(income: float, kids: int):
    """
    Given the income and the number of kids it returns the correct subsidy\n
    If no subsidy is forseen it returns 0
    """
    if ( income <= 2E4 ) :
        return kids * 2000
    if ( income <= 3E4 and kids >= 2) :
        return kids * 1500
    if (  income <= 4E4 and kids >= 3):
        return kids * 1000
    #if all cases fail the default value is zero
    return 0

def main():
    while True:
        if input("Press enter to continue or -1 to exit") == "-1": 
            break
        income : float = float(input("Income : "))
        kids : int  =  int(input("Kids : "))
        subsidy : float = subsidy_calculator(income, kids)
        print(f"For an income of : {income} and {kids} kids the subsidy is {subsidy}\n")

if __name__ == "__main__":
    main()