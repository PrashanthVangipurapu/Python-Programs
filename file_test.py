fo=open("file1.txt",'w')
print ("name of file", fo.name )
a="hello\nworld"
fo.write(a)
fo.close()

b="\nnew text added"
fo=open("file1.txt",'a')
fo.write(b)
fo.close()