#class and objects

class Admission_form:
    student_name=""
    student_age=18
    student_address=""
    student_phone_number=""
    parents_mobile_number=""

    def welcome_message(self):
        print("welcome all")

    def information_message(self):
        print("pls visit our college environment ")

    def printstudent_details(self,student_name,student_age,student_address,student_phone_number,parents_mobile_number):
        print("student details:")
        print("student_name:",student_name)
        print("student_age:",student_age)
        print("student_address:",student_address)
        print("student_phone_number:",student_phone_number)
        print("parents_mobile_number:",parents_mobile_number)



student1=Admission_form()
student1.student_age=22
print(student1.student_name)
student1.welcome_message()
student1.printstudent_details("john",21,"london cross street","6787653","45677654")