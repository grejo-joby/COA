import sys
m=input();q=input();counter=len(m);acc='0000';carry='0'
print("-----------------------------------------------")
print("counter"+" | "+"carry"+" | "+"accu"+"   | "+"   q"+"  | "+"operartion |")
print("-----------------------------------------------")
print(counter,"      |   ",carry," | ",acc," | ",q,"| Initial    |")
print("-----------------------------------------------")
counter-=1;ask=input('enter 1 to continue');sys.stdout.write("\033[F") ,sys.stdout.write("\033[K")
while(ask=='1' and counter!=-1):
	if(q[len(q)-1]=='1'):
		#sum
		sum=str(bin(int(m,2) + int(acc,2))[2:]).zfill(5)
		carry=sum[0]
		acc=sum[1:]	
		print(counter,"      |   ",carry," | ",acc," | ",q,"| add        |")
	else:
		carry=acc[0]
	##rs
	q=(acc[3]+q)[:4]
	acc=(carry+acc)[:4]
	print(counter,"      |   ",carry," | ",acc," | ",q,"| shift      |")
	print("-----------------------------------------------")
	counter-=1;ask=input('enter 1 to continue');sys.stdout.write("\033[F") ;sys.stdout.write("\033[K")