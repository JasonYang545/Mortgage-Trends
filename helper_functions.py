#!/usr/bin/env python
# coding: utf-8

# In[ ]:


bank_district = {
    'Atlanta':['Alabama', 'District of Columbia', 'Florida', 'Georgia', 'Maryland', 'North Carolina', 'South Carolina', 'Virginia'],
    'Cincinnati':['Kentucky', 'Ohio', 'Tennessee'],
    'New York':['New York', 'New Jersey', 'Puerto Rico', 'Virgin Islands'],
    'Boston':['Connecticut', 'Massachusetts', 'New Hampshire', 'Maine', 'Vermont', 'Rhode Island'],
    'Pittsburgh':['Delaware', 'Pennsylvania', 'West Virginia'],
    'Indianapolis':['Indiana', 'Michigan'],
    'Chicago':['Illinois','Wisconsin'],
    'Topeka':['Colorado', 'Kansas', 'Nebraska', 'Oklahoma'],
    'Dallas':['Arkansas', 'Louisiana', 'Mississippi', 'New Mexico', 'Texas'],
    'San Francisco':['Arizona', 'California', 'Nevada'],
    'Des Moines':['Alaska', 'Idaho', 'Iowa', 'Minnesota', 'Missouri', 'Montana', 'North Dakota', 'Oregon', 'South Dakota', 'Utah', 'Washington', 'Wyoming', 'Hawaii', 'Guam', 'American Somoa', 'Northern Mariana Islands']
}

races = {
    1:"White",
    2:"Asian",
    21:"Asian",
    22:"Asian",
    23:"Asian",
    24:"Asian",
    25:"Asian",
    26:"Asian",
    27:"Asian",
    3:"Black",
    4:"Hawaiian/Pacific",
    41:"Hawaiian/Pacific",
    42:"Hawaiian/Pacific",
    43:"Hawaiian/Pacific",
    44:"Hawaiian/Pacific",
    5:"White",
    6:"N/A",
    7:"N/A"
}

def get_bank_name(lei):
    import requests as rq
    URI = f"https://leilookup.gleif.org/api/v2/leirecords?lei={lei}"
    response = rq.get(URI)
    if response == 200:
        data = response.json()
    lei_data = response.json()
    res = [sub['Entity'] for sub in lei_data] 
    res2 = [sub['LegalName'] for sub in res]
    need = res2[0]
    return(need['$'])


def get_bank_cert(lei):    
    import requests as rq
    URI = f"https://leilookup.gleif.org/api/v2/leirecords?lei={lei}"
    response = rq.get(URI)
    if response == 200:
        data = response.json()
    lei_data = response.json()
    res = [sub['Entity'] for sub in lei_data] 
    res2 = [sub['RegistrationAuthority'] for sub in res]
    try:
        res3 = [sub['RegistrationAuthorityEntityID'] for sub in res2]
    except:
        return("None")
    need = res3[0]
    return(need['$'])

