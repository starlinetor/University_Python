
def discount(prices : list[float], is_pet: list[bool]) -> float:
    """
    Returns the discount, at least 5 items and 1 pet, discout is 20% of items
    """
    
    
    pet_counter : int = 0
    
    not_pet_counter : int = 0
    not_pet_price : float = 0
    
    for price, pet in zip(prices, is_pet) : 
    
        #save data
        if pet : 
            #save number of pets bought
            pet_counter += 1
        else :
            #save number of items and price of those items
            not_pet_counter += 1
            not_pet_price += price
        
    #if at least 1 pets and 5 items were sold applay a 20% discount only on other stuff
    
    print(f"{pet_counter = }\n{not_pet_counter = }")
    print(f"{not_pet_price = }\n")
    
    if pet_counter >= 1 and not_pet_counter >= 5 :
        return not_pet_price * 0.2
    #if the discount is not eligible return 0
    return 0

test_price : list[float] = [
    # items
    10,
    20,
    40,
    12.3,
    5465,
    123,
    1236,
    123,
    1
]

test_is_pet : list[bool]= [
    False,
    False,
    False,
    False,
    True,
    False,
    True,
    False,
    False,
]
print(f"{"Test":_^40}")
print(discount(test_price, test_is_pet))
print(f"{"End Test":_^40}\n")

prices : list[float] = []
is_pet : list[bool] = []

while True:
    
    #adding a try except prevents the program from crashing if the input is not a float
    while True : 
        try : 
            price = input("Enter -1 to end or enter price of the item: ")
            price = float(price)
            break
        except ValueError:
            print(f"{price} is an invalid input, only numbers are allowed, exp : '12.43'")
    #if the input is -1 we exit
    if price == -1:
        break
    
    while True:
        pet = input("Pet ? Y/N : ")
        if pet not in ('Y','N'):
            print(f"{pet} is an invalid input, valid inputs : 'Y', 'N'" )
        else:
            break
    
    prices.append(price)
    is_pet.append(True if pet == 'Y' else False)
    
    print()

print()
print(f"Discount : {discount(prices, is_pet)}")