#exercise 3 ranking number

mark=int(input("Enter your mark to calculate your grade "))

if mark>=90:
    print("Grade: A")
elif mark>=75:
    print("Grade: B")
elif mark>=60:
    print("Grade: C")
elif mark>=50:
    print("Grade: D")
elif mark<50 and mark>1:
    print("Grade: F")
elif mark<0:
    print("marks cant be negative")
