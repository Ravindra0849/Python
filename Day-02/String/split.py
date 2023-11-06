
# here we are using Split between the words

text = "python is popular tool"
word = text.split()
print("words:", word) # output is words: ['python', 'is', 'popular', 'tool']

#################################################################################################################################################

# Real time senario example is

# we are having multiple arn in AWS cloud, we need only to identify the users of that arn number. here iam using only one arn for example purpose. so the python script is

arn = "arn:aws:iam::123456789012:user/johndoe"
word = arn.split("/")
print(word) # output is ['arn:aws:iam::123456789012:user', 'johndoe']


#################################################################################################################################################

# we are having multiple arn in AWS cloud, we need only to identify the users of that arn number. here iam using multiple arn for example purpose. so the python script is

arn = "arn:aws:iam::123456789012:user/johndoe", "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-0e9801d129EXAMPLE"
word = tuple(arn[0].split("/")), tuple(arn[1].split("/"))
print(word) # output is (('arn:aws:iam::123456789012:user', 'johndoe'), ('arn:aws:ec2:us-east-1:123456789012:vpc', 'vpc-0e9801d129EXAMPLE'))

#################################################################################################################################################

# This is also one example for multiple ARN's 

arn = "arn:aws:iam::123456789012:user/johndoe", "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-0e9801d129EXAMPLE"
word = (arn[0].split("/")), (arn[1].split("/"))
print(word)