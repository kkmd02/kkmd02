import math


def split_paycheck(pay, transportation = False, TFSA_percent = 0.6):
    ''' pay = float, TFSA_percent = float between [0, 1], transportation = boolean

    split paycheck into categories using the following rules:

        60% TFSA

        Then
        $20 spending
        $20 dating
        $20 gas
        $5 wedding
        $30 transportation

            Then what's left split between
            wedding
            gifts
            tattoos
            trips

            transportation = True iff less than $40 in account


        '''
    split_dict = {
            "TFSA": math.ceil(TFSA_percent *pay),
            "Spending": 20,
            "Dating": 20,
            "Gas": 20,
            "Transportation": 30,
            "Wedding": 5,
            "Gifts": 0,
            "Short-Term Goals": 0,
            "Tattoo": 0,
            "Trips": 0}

    if transportation == True:
        split_dict["Transportation"] += 20

    pay_check = 0

    for category in split_dict:
        pay_check += split_dict[category]

    if pay < pay_check:
        return "Pay too low"


    leftover = pay

    for category in split_dict:
        leftover -= split_dict[category]

    leftover_cat_list = ["Wedding", "Gifts","Short-Term Goals","Tattoo","Trips"]

    if leftover > 0:
        for category in leftover_cat_list:
            split_dict[category] += round(1/len(leftover_cat_list) * leftover, 2)

    if split_dict['Wedding'] != math.floor(split_dict['Wedding']):
        extra = split_dict['Wedding'] - math.floor(split_dict['Wedding'])
        split_dict['Wedding'] = math.floor(split_dict['Wedding'])
        split_dict["Dating"] += extra

    split_str = ""

    leftover = pay
    total_add = 0

    for category in split_dict:
        split_dict[category] = round(split_dict[category], 2)
        split_str += category + ": $" + str(split_dict[category]) + "\n"
        leftover -= split_dict[category]
        total_add += split_dict[category]


    print(split_str,"\n", "Total: $" , str(round(total_add, 2)), "\n", "Pay-Total: $", str(round(pay-total_add, 2)))


def split_paycheck_gifts(pay, transportation = False, TFSA_percent = 0.6):
    ''' pay = float, TFSA_percent = float between [0, 1], transportation = boolean

    Same as above but all leftovers go to gifts


    '''

    split_dict = {
            "TFSA": math.ceil(TFSA_percent *pay),
            "Spending": 20,
            "Dating": 20,
            "Gas": 20,
            "Transportation": 30,
            "Gifts": 0,
            }

    if transportation == True:
        split_dict["Transportation"] += 20

    pay_check = 0

    for category in split_dict:
        pay_check += split_dict[category]

    if pay < pay_check:
        return "Pay too low"


    leftover = pay

    for category in split_dict:
        leftover -= split_dict[category]

    split_dict["Gifts"] = leftover

    split_str = ""

    leftover = pay
    total_add = 0

    for category in split_dict:
        split_dict[category] = round(split_dict[category], 2)
        split_str += category + ": $" + str(split_dict[category]) + "\n"
        leftover -= split_dict[category]
        total_add += split_dict[category]


    print(split_str,"\n", "Total: $" , str(round(total_add, 2)), "\n", "Pay-Total: $", str(round(pay-total_add, 2)))

def split_paycheck_basic(pay, leftover_cat_list = ["Wedding", "Gifts","Short-Term Goals","Tattoo","Trips"], transportation = False, TFSA_percent = 0.6):
    ''' pay = float, TFSA_percent = float between [0, 1], transportation = boolean

    split paycheck into categories using the following rules:

    60% TFSA

    Then
    $20 spending
    $20 dating
    $20 gas
    $5 wedding
    $30 transportation

        Then what's left split between the list

        transportation = True iff less than $40 in account


    '''

    split_dict = {
            "TFSA": math.ceil(TFSA_percent *pay),
            "Spending": 20,
            "Dating": 20,
            "Gas": 20,
            "Transportation": 30,
            "Wedding": 5}

    if transportation == True:
        split_dict["Transportation"] += 20

    pay_check = 0

    for category in split_dict:
        pay_check += split_dict[category]

    if pay < pay_check:
        return "Pay too low"


    leftover = pay

    for category in split_dict:
        leftover -= split_dict[category]

    if leftover > 0:
        for category in leftover_cat_list:
            if category == "Wedding":
                split_dict[category] += round(1/len(leftover_cat_list) * leftover, 2)
            else:
                split_dict[category] = round(1/len(leftover_cat_list) * leftover, 2)
                # divide the leftovers evenly amongst the other categories

    if split_dict['Wedding'] != math.floor(split_dict['Wedding']):
        extra = split_dict['Wedding'] - math.floor(split_dict['Wedding'])
        split_dict['Wedding'] = math.floor(split_dict['Wedding'])
        split_dict["Dating"] += extra

    split_str = ""

    leftover = pay
    total_add = 0

    for category in split_dict:
        split_dict[category] = round(split_dict[category], 2)
        split_str += category + ": $" + str(split_dict[category]) + "\n"
        leftover -= split_dict[category]
        total_add += split_dict[category]


    print(split_str,"\n", "Total: $" , str(round(total_add, 2)), "\n", "Pay-Total: $", str(round(pay-total_add, 2)))

