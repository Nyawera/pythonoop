class Student:
    #  class Student:
    #             full_name = "Nyawera Tut"
    #             year_of_birth = 2000

    #             class student:
    #                 def __init__(self,full_name,year_of_birth):
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self):
         return f"  {self.first_name}{self.last_name}"

    def initials(self):
        return f"{self.first_name[0]}{self.last_name[0]}"     
    def year_of_birth(self):
        return f"2022-{self.age}"                         



                        
                           













# Add these methods to class student - full_name, year_of_birth, initials. Create two instances and verify the work as expected
# Add these methods to class Account - deposit, withdraw. Create two instances of account and verify they work as expected.