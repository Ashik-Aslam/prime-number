


# 1.......... prime number
num=10
count=0
for i in range(2,num):
  if num%i==0:
    count=count+1

if count==0:
  print("prime")
else:
  print("not prime")

