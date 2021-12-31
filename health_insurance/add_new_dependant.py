from core.db.db import db

def add_new_dependant(main_Customer_ssn,list_of_data):
    name = list_of_data[0]
    birth_date = list_of_data[1]
    plane = list_of_data[2]
    main_ssn = main_Customer_ssn

 
    db(f'''INSERT INTO dependant (`name`, birth_date, plane, belongs_to) VALUES("{name}", "{birth_date}", {plane}, "{main_ssn}"); ''')
    return "successfuly"

# add_new_dependant("01234567891234",["ali", "2005-5-17", 2] )
# add_new_dependant("01234567891234",["asmaa", "2007-6-12", 1] )