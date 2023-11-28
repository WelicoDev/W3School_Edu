# Person nomli sinf va usul yarating:firstname lastname printname

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


class Students:
    def __init__(self , first_name , last_name , age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def information(self):
      print(f"{self.first_name}  {self.last_name} . I am {self.age} years old.")

value = Students("Otabek" , "Xurramov" ,20)

value.information()


class CourseEnglish(Students):
    def __init__(self ,first_name , last_name , age ,  study , faculty , course):
        super().__init__(first_name , last_name , age)
        self.study = study
        self.faculty = faculty
        self.course = course

    def welcome(self):
        print("Welcome", self.first_name, self.last_name, f"I am {self.age} years old.")




x = CourseEnglish("Otabek" , "Xurramov" , 20 , "TUIT" , "Software enegeer" , 3)

print('-----------------------------')

print(x.last_name)
print(x.first_name)

print('------------------------------------------------------')

x.welcome()
