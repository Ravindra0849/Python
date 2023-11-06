import re

text = "python is popular tool and versatile tool"
pattern = r"versatile"

search = re.search(pattern, text)

if search:
    print("match is found successfully")
else:
    print("match is not found")  # output is = match is found successfully

#=========================================================================================================================

import re

text = "I have 3 friends whose names is ram sita sai"

pattern = r"hanuman"

search = re.search(pattern, text)

if search:
    print("Hanuman match found successfully")
else:
    print("Hanuman match not found") 


# output is =Hanuman match not found

