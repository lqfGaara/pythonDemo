import re

str = "<Html>dbwuidhkadu2ihdwj</html>"
pattern = "<[\w]*>\w*<[\w]*>"
# 或者
pattern1 = "<[a-zA-Z]*>\w*</[a-zA-Z]*>"
ret = re.match(pattern1, str).group()
print(ret)
str1="阅读量 99999"
ret1=re.search("\d+",str1).group()
print(ret1)