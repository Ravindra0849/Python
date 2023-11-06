import re

text = "Ravi,Hari,Sudheer,Paramesh"

pattern = r","

split_result = re.split(pattern, text)

print("Split_result:", split_result)


# Output is = Split_result: ['Ravi', 'Hari', 'Sudheer', 'Paramesh']

#================================================================================================================================================

import re

text = "python is best tool"

pattern = r" "

split_result = re.split(pattern, text)

print("split_result:", split_result)

# Output is = split_result: ['python', 'is', 'best', 'tool']