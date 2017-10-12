import hashlib
a='abcadfadfafadsfafafa'
b=1123
sha1=hashlib.sha256()#创建hash的sha类
print(sha1)
print(sha1.update(str(a).encode("utf8")))#输入要加密的文字
print(sha1.digest())
print(sha1.hexdigest())#得到加密后的文字

sha2=hashlib.sha256()
print(sha2)
print(sha2.update(str(b).encode("utf8")))
print(sha2.digest())
print(sha2.hexdigest())


