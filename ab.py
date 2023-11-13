f=open("hello.py",'r')

f1=open("demo.txt",'w')
f1.write("Amal Benny")

l=f.readline()
while l:
	f1.write(l)
	l=f.readline()
f1=open("demo.txt",'r')
print(f1.read())
