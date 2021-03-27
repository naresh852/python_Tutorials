name=input()
rev_name=name[::-1]
if name.lower()==rev_name.lower():
    print('palindorme',rev_name)
else:
    print('not palindrome',name)
