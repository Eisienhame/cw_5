from hh_api import getdata_hh

def get_vacancies_in_table(name):
    pass

i = getdata_hh()
print(len(i[0]))
for n in range(len(i[0])):
    print(i[0]['items'][n]) 