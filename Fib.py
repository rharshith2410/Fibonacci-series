n  = int(input("Enter the number of terms you want"))
i,j = 0,1
count = 0
if n<=0:
	print("invalid input!")
elif n==1:
	print(i)
else :
    str = "FIBBONACCI"
    print(str.center(20,'*'))
    while count<=n:
    	print(i)
    	c = i+j
    	i = j
    	j = c
    	count+=1
