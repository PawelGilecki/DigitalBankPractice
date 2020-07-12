import random

postal_1 = random.randint(0, 100)
postal_1 = f'{postal_1:02}'
postal_2 = random.randint(0, 1000)
postal_2 = f'{postal_2:03}'

def generatePostalCode():
    return(postal_1+"-"+postal_2)