class Students:
    def __init__(self,first_name , last_name , age , gender , address , study , faculty , course , gpa):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.address = address
        self.study = study
        self.faculty = faculty
        self.course = course
        self.gpa = gpa

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

    def welcome(self):
        return  f"Assalom aleykum {self.first_name} {self.last_name}"

    def study_info(self):
        return f"{self.study} {self.faculty} {self.faculty} {self.gpa}"

talabalar = Students("Otabek" , "Xurramov" , 20 , "male" ,"Olmazor , Tashkent" , "TUIT" ,"Software enegeeer" ,3 , 3.84)

talabalar.last_name = "Xakimjonov"
talabalar.age = 19
# del talabalar.gpa

print(talabalar)
print(talabalar.address)

# del talabalar

