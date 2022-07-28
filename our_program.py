import sys

# create a function that checks if it's a number and if has the right length
def validNumber():
    if len(raw_phone_number) != 10: #length of 10, strictly
        return False
    elif not raw_phone_number.isdigit(): #isalnum check if there are only numbers
        return False
    return True

for line in sys.stdin:
    raw_phone_number = line.strip()
    area_code = raw_phone_number[0:3]
    first_three = raw_phone_number[3:6]
    last_four = raw_phone_number[6:]
    if validNumber() is False:
        print("Wrong number inserted")
    else: print('(%s) %s - %s' % (area_code, first_three, last_four))