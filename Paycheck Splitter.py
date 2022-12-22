import math

def split_paycheck(pay, transportation = False, TFSA_percent = 0.65, leftover_cat_list = ["Emergency Fund", "Gifts","Short-Term Goals","Tattoo","Trips"]):
    ''' pay = float, TFSA_percent = float between [0, 1], transportation = boolean

    split paycheck into categories using the following rules:

    60% TFSA

    Then
    
    $20 spending
    $20 dating
    $20 gas
    $5 Emergency Fund
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
            "Emergency Fund": 5}

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
            if category == "Emergency Fund":
                split_dict[category] += round(1/len(leftover_cat_list) * leftover, 2)
            else:
                split_dict[category] = round(1/len(leftover_cat_list) * leftover, 2)
                # divide the leftovers evenly amongst the other categories

    # if split_dict['Wedding'] != math.floor(split_dict['Wedding']):
    #     extra = split_dict['Wedding'] - math.floor(split_dict['Wedding'])
    #     split_dict['Wedding'] = math.floor(split_dict['Wedding'])
    #     split_dict["Dating"] += extra

    split_str = ""

    leftover = pay
    total_add = 0

    for category in split_dict:
        split_dict[category] = round(split_dict[category], 2)
        split_str += category + ": $" + str(split_dict[category]) + "\n"
        leftover -= split_dict[category]
        total_add += split_dict[category]


    print(split_str,"\n", "Total: $" , str(round(total_add, 2)), "\n", "Pay-Total: $", str(round(pay-total_add, 2)))
