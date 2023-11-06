import re

text = "the quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("pattern found:", search.group())
else:
    print("pattern not found")  # Output will be = pattern found: brown

######################################################################################################################


# Here we are writing it for another syntax with another example

import re

text = "Someone as working as a DevOps Engineer with 4 Years of Exp"
pattern = r"DevOps"

search = re.search(pattern, text)
if search:
    print("pattern found:", search.group())
else:
    print("pattern not found") # Output will be = pattern found: DevOps

############################################################################################################################### 


# For Pattern not found sentence is

import re

text = "Someone as working as a DevOps Engineer with 4 Years of Exp"
pattern = r"AWS"

search = re.search(pattern, text)
if search:
    print("pattern found:", search.group())
else:
    print("pattern not found:", pattern) # Output will be = pattern not found: AWS