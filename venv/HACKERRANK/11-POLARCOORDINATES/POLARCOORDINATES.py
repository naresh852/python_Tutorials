import cmath
s=complex(input())
x=s[0]
y=s[1]
z=cmath.sqrt((x*x)+(y*y))
print(*cmath.polar(z))
print(cmath.phase(s))

# import cmath
print(*cmath.polar(complex(input())), sep='\n')