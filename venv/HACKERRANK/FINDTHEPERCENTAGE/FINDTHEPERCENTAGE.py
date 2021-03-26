if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

print(student_marks.get(query_name))
l1=student_marks.get(query_name)
length=len(l1)
sum=0
for index in l1:
    sum=sum+index
result = sum/length
print("{0:0.2f}".format(result))
