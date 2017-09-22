# python集合Set详解
a=set("dfwefer12321")
b=set("jyghjtyhtryrt21")
# 集合的交集
c=a&b
print(c)
# 集合的并集
d=a|b
print(d)
# 集合的差集
e=a-b
print(e)
#对称差集(在a或b中，但不会同时出现在二者中)
f=a^b
print(f)