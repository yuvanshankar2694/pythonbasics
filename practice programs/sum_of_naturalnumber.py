#this will give the sum of natural numbers using a while and for loop

number=int(input("enter a number : "))
# sum=0
# count=1
# while count<=number:
#     sum=sum+count
#     count=count+1
#
# print(sum)


#using while loop

sum=0
for i in range(1,number+1):
    sum=sum+i
    print(i)
print(sum)