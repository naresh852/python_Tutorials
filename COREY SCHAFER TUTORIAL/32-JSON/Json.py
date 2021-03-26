#Datan format for storing some information
# #fecthing data from online Api and also used for online configuration
#json ====== JAVASCRIPT OBJECT NOTATION
import json
# people_string='''
# {
# "people":[
#        {"name":"John Smith",
#         "phone":"615-555-7164",
#         "emails":["johnsmith@bogusemail.com","john.smith@work-place.com"],
#          "has_license":false
#         },
#         {
#          "name":"Jane Doe",
#           "phone":"560-555-5135",
#           "emails":null,
#            "has_license":true
#          }
#         ]
# }
# '''
'''loads method loads a string{from string}
load method  to a  json file{from jsonfile}'''
#json data to python data conversion
# data=json.loads(people_string)
# # print(data)
# # print(type(data))
# for person in data["people"]:
#     # print(person["name"])
#     #  print(person)
#     del person['phone']
#     # print(person)
# # print(data)
'''to json dataconversion use dump
 use dumps to jsonstring'''
# # print()
# new_string=json.dumps(data,indent=2,sort_keys=True)
# print(new_string)

#new json file parsing and using
with open('states.json') as f:
    data=json.load(f)
# for state in data["states"]:
    # print(state['name'],state['abbreviation'])
    #  del state['area_codes']
    # print(state)
with open('new_data.json','w') as f:
    json.dump(data,f,indent=2)
