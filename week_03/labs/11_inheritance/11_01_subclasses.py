'''
Build on 10_03_freeform_classes from the section on Classes, Objects and
Methods.
Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in 10_03_freeform_classes.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

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

    def __init__(self, sport_name="Chicago Bears", number_of_playes=11, way_of_winning="scoring more!"):
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



class ChicagoSox(SportsTeam):
    def __init__(self):
        sports_name = "baseball"
        number_of_players = 9
        ways_of_winning = "Score more runs than opponent"
        SportsTeam.__init__(self, sports_name, number_of_players, way_of_winning)

class BirminghamBarons(ChicagoSox):
    def __init__(self):
        sports_name = "baseball"
        number_of_players = 9
        ways_of_winning = "Score more runs than opponent"
        ChicagoSox.__init__(self, sports_name, number_of_players, way_of_winning)



class Employee():
    """a person employed for wages or salary, especially at non-executive level.
Attributes:
            age (int): Description
            sex (str): Description
            years with company (int) : Description
    """
    purpose = "Perform work to collect income"
    attire = "uniform"
    def __init__(self, age=30, sex="N/A", tenure=0):
        self.age = age
        self.sex = sex
        self.tenure = tenure

    def description(self, employee_number):
        return f"Employee # {employee_number} is a {self.age} year old {self.sex} who has worked {self.tenure} years with the company"
    def __str__(self):
        return f"{self.age} | {self.sex} | {self.tenure}"

class Salaried(Employee):
    def __init__(self, payment):
        def __init__(self):
        age = age
        sex = "sex"
        tenure = tenure
        self.payment = "salaried"
    Employee.__init__(self, age, sex, tenure):

class UnSalaried(Employee):
    def __init__(self, payment):
        def __init__(self):
        age = age
        sex = "sex"
        tenure = tenure
        self.payement = "hourly"
    Employee.__init__(self, age, sex, tenure):


