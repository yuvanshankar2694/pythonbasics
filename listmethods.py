#lesson 11 list and its methods

#append is used to add value at the end of the list
list=["rib","heart","lungs","spinal cord","liver"]
list.append("brian")
print(list)

#insert is used to add values between the lists
list.insert(2,"skull")
print(list)

#remove is used to remove the values in the list we need to give value that will find out and the
# and removes the value in the list
list.remove("liver")
list.remove("spinal cord")
print(list)

#clear method is used to remove all from the list
# list.clear()
# print(list)

#reverse method is used to reverse the list
list.reverse()
print(list)

# to return the length of the functions
print(len(list))