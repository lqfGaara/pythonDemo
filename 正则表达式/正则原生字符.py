import re

mm = "c:\\a\\b\\c"
ret = re.match("c:\\\\a", mm).group()
print(ret)

ret1 = re.match(r"c:\\a", mm).group()
print(ret1)
# Python中字符串前面加上r表示原生字符串这样"c:\\a"中的\就表示的是一个字符
# 而不是一个转意字符。
