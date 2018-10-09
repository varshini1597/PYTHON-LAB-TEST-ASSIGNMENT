import sys
args=sys.argv[1]
f=open('ipvertical.txt',"r")
line=f.readline()
#print(line)
count=0    
for line in f:
	if args in line:
		count=count+1
if(count>0):
	print("IP found")
	print("number of times IP found is",count)
else:
	print("IP not found")
sys.exit()