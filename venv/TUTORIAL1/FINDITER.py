# re.finditer(pattern, string, flags=0)
import re
s1 = 'Blue Berries'
pattern = 'Blue Berries'
for match in re.finditer(pattern, s1):
    s = match.start()
    e = match.end()
    print ("String match %s at %d:%d" % (s1[s:e], s, e))
    