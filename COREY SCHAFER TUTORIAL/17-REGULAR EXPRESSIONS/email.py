import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

# pattern = re.compile(r'[\w]+@\w+\.\w+')
pattern=re.compile(r'[a-zA-Z0-9-.*]+@[a-zA-Z0-9-.*]+\.[a-zA-Z0-9-.*]+')
matches = pattern.finditer(emails)

for match in matches:
    print(match)
