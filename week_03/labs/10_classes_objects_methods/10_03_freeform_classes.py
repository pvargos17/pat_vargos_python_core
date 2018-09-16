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
        """
            Describes the Sports Team with # of championships

            Args:
            Sport (str): Description
            way_of_winning (str): Description
            number_of_playes (int) : Description

            Returns:
                str: a sentence describing the Sports team
        """
        return f"{self.sport_name} have {numer_of_championships} championship(s), & have {self.number_of_playes} players and win games by {self.way_of_winning}"

    def __str__(self):
        return f"{self.sport_name} | {self.number_of_playes} | {self.way_of_winning}"



#class WhiteSox():
    """The Chicago White Sox are an American professional baseball team based in Chicago, Illinois
Attributes:
            sport (str): Description
            way_of_winning (str): Description
            number_of_playes (int) : Description
    """





#class BirminghamBarons():
    """The Birmingham Barons are a Minor League Baseball team based in Birmingham, Alabama.
        The team, which plays in the Southern League,is the Double-A affiliate of the Chicago White
         Sox and plays at Regions Field in downtown Birmingham
Attributes:
            sport (str): Description
            way_of_winning (str): Description
            number_of_playes (int) : Description
    """


Chi_Bears = SportsTeam("DA BEARS", "11", "being monsters of the midway")
Chi_Flubs = SportsTeam("The Flubs","no class ", "stealing Theo or else they would go back to sucking!")
print(Chi_Bears.description(1))
print(Chi_Flubs.description(2))
print(Chi_Bears)
