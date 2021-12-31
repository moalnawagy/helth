from add_new_hospital import add_new_hospital
from add_new_customer import add_new_customer
from add_new_dependant import add_new_dependant
from hospitals_on_plane import hospitals_on_plane


def add_hospital_core(name, phone, address, email, website,*planes ):
    data = [name, phone, address, email, website]
    l_planes = list(planes)
    add_new_hospital(data, l_planes)


def add_new_customer_core(ssn,name, birth_date, gender, income, address, phone, has_chronic_dis, tall, weight, email, plane):

    data = [ssn, name, birth_date, gender, income, address, phone, has_chronic_dis, tall, weight, email, plane]
    add_new_customer(data)

def add_dependent_core(ssn, name, birth_date, plane):
    data =[name, birth_date, plane]
    return add_new_dependant(ssn, data)

def hospital_on_plane_core(p):
    hospitals_on_plane(p)


