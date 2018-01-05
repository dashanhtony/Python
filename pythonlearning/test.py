import sys,os
print(sys.path)

print(os.path.join(sys.path[5],"\\","abc"))
print (sys.path[5].replace("\\","/"))