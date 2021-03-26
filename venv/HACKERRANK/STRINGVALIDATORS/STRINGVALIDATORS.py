# s = input()
# # l=list(s)
# alphanum=False
# alpha=False
# digits=False
# lower=False
# upper=False
# for i in range(len(s)):
#     if lower==False:
#         if s[i].islower()==True:
#             lower=True
#             alpha=True
#     if digits==False:
#         if s[i].isdigit()==True:
#             digits=True
#
#     if upper==False:
#         if s[i].isupper()==True:
#             upper=True
#             alpha=True
#     if alpha==True or digits==True:
#         alphanum=True
#
#
# print(alphanum)
# print(alpha)
# print(digits)
# print(lower)
# print(upper)
# ALTERNATE SOLUTION USING ANY FUNCTION
str = input()
print (any(c.isalnum()  for c in str))
print (any(c.isalpha() for c in str))
print (any(c.isdigit() for c in str))
print (any(c.islower() for c in str))
print (any(c.isupper() for c in str))