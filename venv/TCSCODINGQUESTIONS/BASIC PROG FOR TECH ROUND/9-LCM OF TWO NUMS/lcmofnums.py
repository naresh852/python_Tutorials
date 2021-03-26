#smalles common multiple
#smallest non zero common number which is a multiple of booth numbers
'https://www.youtube.com/watch?v=6ykRY6bHVX0'
n1=int(input())
n2=int(input())

if n1>n2:
    higher=n1
else:
    higher=n2
value=higher
while True:
    if higher%n1==0 and higher%n2==0:
        print('lcm is',higher)
        break
    else:
        higher+=value