import re
s1="http://www.interoem.com/messageinfo.asp?id=35"
s2="http://3995503.com/class/class09/news_show.asp?id=14"
s3="http://lib.wzmc.edu.cn/news/onews.asp?id=769"
s4="http://www.zy-ls.com/alfx.asp?newsid=377&id=6"
s5="http://www.fincm.com/newslist.asp?id=415"
s="http://www.interoem.com/messageinfo.asp?id=35http://3995503.com/class/class09/news_show.asp?id=14http://lib.wzmc.edu.cn/news/onews.asp?id=769http://www.zy-ls.com/alfx.asp?newsid=377&id=6http://www.fincm.com/newslist.asp?id=415"
paterrn ="(^http://(\w.*)+(com|cn)/)+"
r=re.match(paterrn,s3).group()
ll=re.split("http",s)
print(r)
print(ll)