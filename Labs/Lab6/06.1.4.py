def interest_calculator (years: int, balance: float, interest: float) -> float:
    """
    Returns the total balance after interest has been applyed for a precise number of years\n
    :Param:\n
    years - years of interest\n
    balance - starting balance\n
    interest - interest to be applyed each year 7% = 0.7\n
    :Return:\n
    float - new balance after x years have passed with x interest rate 
    """ 
    for i in range(years):
        balance *= (1+interest)
        
    return balance