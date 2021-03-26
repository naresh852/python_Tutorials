import csv
output_html=""
names=[]
with open('eg.csv' ,'r') as data_file:
     # csv_data=csv.reader(data_file,delimiter='\t')
     csv_data=csv.DictReader(data_file,delimiter='\t')

     #we dont want first headers
     # next(csv_data)
     next(csv_data)
     for line in csv_data:
         if line['FirstName']=='No Reward':
             break
         names.append(f"{line['FirstName']} {line['LastName']}")
     #      print(line)
     # print(list(csv_data))
print(len(names))
output_html+=f'<p>currently there are {len(names)} contributors to site.Thank you!</p>'
# for name in names:
#     print(name)
output_html+='\n<ul>'
for name in names:
    output_html+=f'\n\t<li>{name}</li>'
output_html+='\n</ul>'
print(output_html)
