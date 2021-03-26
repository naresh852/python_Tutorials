import json
from urllib.request import urlopen
with urlopen("https://petnames.com/names/search.php?a=A") as response:
    source=response.read()
# print(source)
data=json.load(source)
print(json.dumps(data,indent=2))