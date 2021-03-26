'''num=input()
# num=[int(digit) for digit in nu]

product=1
for i in num:
    product=product*int(i)
print(product)'''

# sort a string separated by a '.'
st=input().split('.')
st.sort()
x2=".".join(st)
print(x2)