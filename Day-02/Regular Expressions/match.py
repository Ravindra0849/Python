import re

text = "python is a popular tool"
pattern = r"python"

match = re.match(pattern, text)
if match:
    print("pattern found:", match.group())
else:
    print("match not found") # output is = pattern found: python

###################################################################################################################################

# Another example for this one

import re

text = "python is popular and Versatile tool"
pattern = r"versatile" # here v is small letter
match = re.match(pattern, text)
if match:
    print("match found:", match)
else:
    print("match not found") # output is match not found, We give "V" it shows match found.


