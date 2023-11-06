
# Substring is used for to search any word is there in the given text/file. it checks the whole file and give the output.
# In real time we are using this one regularlly in log files and some another files.
# In log files we can use this senario we can easily access the Error handling logs with huge output.

text = "python is a popular and versitile tool"
substring = "popular"
if substring in text:
    print(substring, "found in text")
else:
    print("match not found")
    
# In above text we have popular word it shows the output is = popular found in text

#===============================================================================================================================================


text = "python is a popular and versitile tool"
substring = "awesome"
if substring in text:
    print(substring, "found in text")
else:
    print("match not found")
    
# Here awesome word is not mentioned in text, so output is = match not found