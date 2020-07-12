import random

SSN_1 = random.randint(0, 1000)
SSN_1 = f'{SSN_1:03}'
SSN_2 = random.randint(0, 100)
SSN_2 = f'{SSN_2:02}'
SSN_3 = random.randint(0, 10000)
SSN_3 = f'{SSN_3:04}'

def generateSSN():
    return(SSN_1+"-"+SSN_2+"-"+SSN_3)