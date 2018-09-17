'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...

'''
class SportsTeam():
    """A sports team is a group of individuals who play sports, usually team sports, on the same team
Attributes:
            sport (str): Description
            way_of_winning (str): Description
            number_of_playes (int) : Description
    """
    objective = "Win!"
    location = "stadium"

    def __init__(self, sport_name="Chicago Bears", number_of_playes="11", way_of_winning="scoring more!"):
        self.sport_name = sport_name
        self.number_of_playes = number_of_playes
        self.way_of_winning = way_of_winning

    def description(self, numer_of_championships):
        """Describes the Sports Team with # of championships

            Args:
            Sport (str): Description
            way_of_winning (str): Description
            number_of_playes (int) : Description

            Returns:
                str: a sentence describing the Sports team
        """
        return f"{self.sport_name} have {numer_of_championships} championship(s), have {self.number_of_playes} players, and win games by {self.way_of_winning}"

    def __str__(self):
        return f"{self.sport_name} | {self.number_of_playes} | {self.way_of_winning}"



class Employee():
    """a person employed for wages or salary, especially at non-executive level.
Attributes:
            age (str): Description
            sex (str): Description
            years with company (int) : Description
    """
    purpose = "Perform work to collect income"
    attire = "uniform"
    def __init__(self, age="30", sex="N/A", tenure="0"):
        self.age = age
        self.sex = sex
        self.tenure = tenure

    def description(self, employee_number):
        return f"Employee # {employee_number} is a {self.age} year old {self.sex} who has worked {self.tenure} years with the company"
    def __str__(self):
        return f"{self.age} | {self.sex} | {self.tenure}"



class Student():
    """a person who is studying at a university or other place of higher education
    Attributes:
        name(str) = Description
        age(str) = Description
        ID_num (str) = Description
    """


    def __init__(self, name="Bob", sex="N/A", id_num="18"):
        self.name = name
        self.sex = sex
        self.id_num = id_num

    def description(self, school_year):
        return f"{self.name} is student # {self.id_num}, who is a {self.sex} {school_year}"
    def __str__(self):
        return f"{self.name} | {self.sex} | {self.id_num}"

Chi_Bears = SportsTeam("DA BEARS", "11", "being monsters of the midway")
Chi_Flubs = SportsTeam("The Flubs","no class ", "stealing Theo or else they would go back to sucking!")
print(Chi_Bears.description(1))
print(Chi_Flubs.description(2))
print(Chi_Bears)
Mark = Employee("26", "Male", "4")
Michelle = Employee("27", "Female", "9")
print(Mark.description(17))
print(Michelle.description(31))
print(Mark)
Emily = Student("Emily", "Female", "17")
Art = Student("Art", "Male", "21")
print(Emily.description("Freshman"))
print(Emily)

