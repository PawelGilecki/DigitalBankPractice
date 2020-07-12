import random

mobile_1 = str(random.randint(501, 900))
mobile_2 = random.randint(0, 1000)
mobile_2 = f'{mobile_2:03}'
mobile_3 = random.randint(0, 1000)
mobile_3 = f'{mobile_3:03}'

phone_1 = random.randint(0, 100)
phone_1 = f'{phone_1:02}'
phone_2 = str(random.randint(101, 1000))
phone_3 = random.randint(0, 100)
phone_3 = f'{phone_3:02}'
phone_4 = random.randint(0, 100)
phone_4 = f'{phone_4:02}'

work_phone_1 = random.randint(0, 100)
work_phone_1 = f'{work_phone_1:02}'
work_phone_2 = str(random.randint(101, 1000))
work_phone_3 = random.randint(0, 100)
work_phone_3 = f'{work_phone_3:02}'
work_phone_4 = random.randint(0, 100)
work_phone_4 = f'{work_phone_4:02}'


def generateMobile():
    return(mobile_1+"-"+mobile_2+"-"+mobile_3)

def generateHomePhone():
    return(phone_1+" "+phone_2+" "+phone_3+" "+phone_4)

def generateWorkPhone():
    return(work_phone_1+" "+work_phone_2+" "+work_phone_3+" "+work_phone_4)