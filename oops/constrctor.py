#oops chapter 2

class Mobile:

    def __init__(self,name=None):
        if name:
            self.mobile_name=name
        else:
            print("default constrcutor is called")

Mobile1=Mobile()

Mobile2=Mobile("samsung")
print(Mobile2.mobile_name)


# __init__ -> like that only we will initialize constructor in python
#__init__ -> only one init is allowed for 1 class