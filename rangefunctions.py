#lesson 13 range functions

#range function is used to print the number in a particular range 10-1 9 values 0-9 will be there
numbers =range(5)
print("1 value range")
for i in numbers:
    print(i)
#we can give range in many ways like range(5,9) it will give output like 5,6,7,8
print("2 value range")
for item in range(5,9):
    print(item)

# we can able to see 3 values there the last values skips it will give output like 0,2,4
print("3 value range")
for item in range(0,5,2):
    print(item)

#mostly we will use range in for loop not sepertedly