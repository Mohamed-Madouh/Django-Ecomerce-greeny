import random

def grnerate_code():
    length = 8
    number='0123456789'
    code = ''.join(random.choice(number)  for x in range(length))
    return code