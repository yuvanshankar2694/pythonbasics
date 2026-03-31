#lesson 11 list and its methods

#append is used to add value at the end of the list
lists=["rib","heart","lungs","spinal cord","liver"]
lists.append("brian")
print(lists)

#insert is used to add values between the lists
lists.insert(2,"skull")
print(lists)

#remove is used to remove the values in the list we need to give value that will find out and the
# and removes the value in the list
lists.remove("liver")
lists.remove("spinal cord")
print(lists)

#clear method is used to remove all from the list
# list.clear()
# print(list)

#reverse method is used to reverse the list
lists.reverse()
print(lists)

# to return the length of the functions
print(len(lists))

#clear the list
# list.clear()

#copy list
copy_list:list[str]=lists.copy()
lists.remove("rib")
print(lists)
print(copy_list)

#count the occurances of the objects
occ=lists.count("skull")
print(occ)

#extend or 2 lists
list1=["kidney","nerves"]
lists.extend(list1)
print(lists)

#insert at specific position
lists.insert(2,"teeth")
print(lists)

#sort the lists
lists.sort()
print(lists)