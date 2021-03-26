#coma separated values
#how to read,parse,write
#can be dash,or tab separated values,commas are delimiters
import csv
# with open('new_csv','r') as csvfile:
#     csvreader=csv.reader(csvfile,delimiter='\t')
#     for line in csvreader:
#         print(line)
# with open('names.csv','r') as csvfile:
#     csvreader=csv.reader(csvfile)
#     # for line in csvreader:
#     #     print(line)
#     # next(csvreader)
#     with open('new_csv','w') as newfile:
#         csvwriter=csv.writer(newfile,delimiter='\t')
#         for line in csvreader:
#         # print(line)
#         #    print(line[2])
#              csvwriter.writerow(line)
# with open('names.csv','r') as csvfile:
#      csvreader=csv.DictReader(csvfile)
#      for line in csvreader:
#          print(line)
with open('names.csv','r') as csvfile:
     csvreader=csv.DictReader(csvfile)
     with open('new_csv','w') as newfile:
         # fieldnames=['first_name','last_name','email']
         fieldnames = ['first_name', 'last_name']
         csvwriter=csv.DictWriter(newfile,fieldnames=fieldnames,delimiter='\t')
         csvwriter.writeheader()
         for line in csvreader:
             del line['email']
             csvwriter.writerow(line)