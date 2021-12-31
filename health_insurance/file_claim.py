from core.db.db import db
from get_customer_id import get_customer_id
# list = [amount, date, descreption, main_CUstomer_ssn, dependent = 0(if it's not for dependent), hospital ]
def file_claim(list_of_data):
    amount = list_of_data[0]
    date = list_of_data[1]
    descreption = list_of_data[2]
    mainly_for = list_of_data[3]
    C_id = get_customer_id(mainly_for)
    dependent = list_of_data[4]
    hospital = list_of_data[5]
    hospital_id = db(f'''SELECT H_ID FROM hospital WHERE H_name LIKE "%{hospital}%"''')[0][0]
    if dependent ==0:
        db(f'''INSERT INTO insurance_claim (amount, date, description, mainly_for, hospital) VALUES ({amount}, "{date}", "{descreption}", {C_id},{hospital_id} );''')
    else:
        dep_id = db(f'''SELECT D_id FROM dependant WHERE (belongs_to = "{mainly_for}" AND `name` LIKE "%{dependent}%" )''')[0][0]
        db(f'''INSERT INTO insurance_claim (amount, date, description, mainly_for, dependant, hospital) VALUES ({amount}, "{date}", "{descreption}", {C_id}, {dep_id}, {hospital_id} );''')
    return "successfuly"

# list1 = [2000, "2021-12-23", "this is a description", "01234567820144",0, "Kenana"]
# list2 = [2000, "2021-12-23", "this is a description", "01234567891234", "ali", "Kenana"]
# file_claim(list1)