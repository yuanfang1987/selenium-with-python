import os
import json


f = open("F:\\yuanfang.txt")
c = f.read()
print(c)

j = json.loads(c)

print("value is:",j["id"])

fatherdir = os.path.abspath('..')
print(fatherdir)

newdir = fatherdir + r"\report"

flag = (os.path.exists(newdir))

if not flag:
    os.mkdir(newdir)
    print("make a new dir....")
else:
    print("dir already exist:",newdir)