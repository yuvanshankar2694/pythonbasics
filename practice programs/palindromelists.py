#palindrome lists ex [1,2,2,1] if u read this reverse its also the same

palin=[1,2,2,1]

print(palin)
palin.reverse()
print(palin)
if palin==palin[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#[::-1] check until the zeroth element last to first