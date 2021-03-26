points = { 'A+' :4.0, 'A' :4.0, 'A-' :3.67, 'B+' :3.33, 'B' :3.0, 'B-' :2.67,
'C+' :2.33, 'C' :2.0, 'C' :1.67, 'D+' :1.33, 'D' :1.0, 'F' :0.0}
numcourses = 0
totalpoints = 0
done = False
while not done:
    grade = input( ) # read line from user
    if grade == '': # empty line was entered
        done = True
    elif grade not in points: # unrecognized grade entered
        print("Unknown grade {0} being ignored".format(grade))
    else:
        numcourses += 1
        totalpoints += points[grade]
if numcourses > 0: # avoid division by zero
    print('Your GPA is {0:.3}'.format(totalpoints / numcourses))