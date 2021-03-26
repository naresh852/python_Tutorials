# re.compile(pattern, repl, string):
import re
pattern=re.compile('TP')
result=pattern.findall('TP Tutorialspoint TP')
print (result)
result2=pattern.findall('TP is most popular tutorials site of India')
print (result2)
# We can combine a regular expression pattern into pattern objects,
# which can be used for pattern matching. It also helps to search a pattern again without rewriting it.