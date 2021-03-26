
# REGULAR EXPE THEY ALLOW US TO SEARCH AND MATCH SPECIFIC PATTERN OF tEXT:
import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
Ha^Ha&&Ha
HaHa--HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
cat
pat
mat
bat
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
sentence='START a sentence and then bring to it to an end'
#pattern=re.compile('\.')
#doesnt work without backslash for .
#pattern=re.compile('.')
# pattern=re.compile(r'abc')
# pattern=re.compile('coreyms\.com')
# pattern=re.compile(r'\bHa')
# pattern=re.compile(r'\BHa')
# pattern=re.compile(r'^start')
# pattern=re.compile(r'end$')
# pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#character set
# pattern=re.compile(r\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# pattern=re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
#find from a-b
# pattern=re.compile(r'[1-5]')
# pattern=re.compile(r'[a-zA-Z]')
#everything not a lower case and upper case
# pattern=re.compile(r'[^a-zA-Z]')
# pattern=re.compile(r'[^b]at')
#quantifiers
# pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern=re.compile(r'M[r]?[s]?[\.]?\s[A-Z]\w*')
#groups in regex
# pattern=re.compile(r'M(r|s|rs)[\.]?\s\w*')
# pattern=re.compile(r'start')
#FLAGS IN REGEX
# pattern=re.compile(r'start',re.IGNORECASE)
pattern=re.compile(r'start',re.I)
# pattern=re.compile(r'sentence')
# matches=pattern.finditer(text_to_search)
# matches=pattern.finditer(sentence)
# matches=pattern.findall(text_to_search)
matches=pattern.match(sentence)
# # matches=pattern.search(sentence)
# for match in matches:
#     print(match)
print(matches)

# with open('data.txt','r') as f:
#     contents=f.read()
#     matches=pattern.finditer(contents)
#     for match in matches:
#         print(match)

