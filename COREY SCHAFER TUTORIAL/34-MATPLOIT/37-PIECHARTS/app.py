from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
slices=[60,20,10,26,80,66]
# slices=[59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript',
#           'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
colors=['blue','red','yellow','green','black','white']
labels=['sixty','twenty','ex1','ex2','ex3','ex4']
explode=[0,0,0,0.5,0,0]
plt.pie(slices,labels=labels,explode=explode,colors=colors,shadow=True,startangle=60,autopct='%1.1f%%',wedgeprops={'edgecolor':'white'})
# plt.pie(slices,labels=labels,wedgeprops={'edgecolor':'white'})
plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
# Language Popularity
# slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']