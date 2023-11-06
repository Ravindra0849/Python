import re

text = "python is a popular tool"

pattern = r"popular"

replacement = "Demanding"

new_text = re.sub(pattern, replacement, text)

print("modified text:", new_text)  # output is = modified text: python is a Demanding tool

#=====================================================================================================================

# Another way is 

import re

text = "python is a popular tool"

pattern = r"popular"

replacement = "Demanding"

new_text = re.sub(pattern, replacement, text)
new_text = str.replace(pattern, replacement, text)  # by using this which text may be changed we identify that one

print("modified text:", new_text)  # output is = modified text: python is a Demanding tool, and modified text: popular