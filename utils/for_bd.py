from hh_api import getdata_hh

def get_vacancies_in_table(id):
    #data = getdata_hh()
    pass

i = getdata_hh()
print(len(i[0]))

for n in range(len(i[0])):
    #print(i[0]['items'][n])
    print(i[0]['items'][n]['id'], i[0]['items'][n]['name'], i[0]['items'][n]['salary'], i[0]['items'][n]['url'])
    print(i[0]['items'][n]['employer']['id'], i[0]['items'][n]['employer']['name'])