__author__ = 'yiqing'

import re

line = "Cats are smarter then dogs "

matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)

if matchObj:
    print("matchObj.group",matchObj.group())
    print("matchObj.groups(1):",matchObj.group(1))
    print("matchObj.groups(2):",matchObj.group(2))

else:
    print("No match!")


searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print( "searchObj.group() : ", searchObj.group())
   print( "searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")


#  deference between search and match:
# match checks for a match only at the beginning of the string,
# while search checks for a match anywhere in the string (this is what Perl does by default)
matchObj = re.match(r"dogs",line,re.M|re.I)

if matchObj:
    print("match -> matchObj.group(): ",matchObj.group())
else:
    print("No match!")
    matchObj = re.match(r".*(dogs).*",line,re.M|re.I)
    if matchObj:
        print("match--->matchObj.group: ",matchObj.group())
        print("all match--->matchObj.groups: ",matchObj.groups())
    else:
        print("no matching too! ")

searchObj = re.search(r"dogs",line,re.M|re.I)
if searchObj:
    print("search--->searchObj.group: ",searchObj.group())
else:
    print("Nothing found!")


# search and replace
phone = "2004-959-559 # this is a phone number"

# 删除python风格的注释
num = re.sub(r"#.*$","",phone)
print("phone num ",num)
# 删除除过数字的所有东西
num = re.sub(r"\D","",phone)
print("phone num : " ,num)