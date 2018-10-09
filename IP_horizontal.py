import sys
args=sys.argv[1]
count=0
file=open("iphorizontal.txt","r")
f=file.readline()
file_list=f.split(" ")
print("list of IP's is:",file_list)
for line in file_list:
  if(args==line):
  	#print("ip found in list:",line)
  	count=count+1;
if(count>0):
 	print("Ip found")
 	print("number of times ip found is:",count)

else:
 	print("Ip not found")