## Classes and OOP

- What is a class?

a programmer-defined type

- How do you define a new class called `MyFirstClass`?

Class MyfirstClass:

- How do you create an object of the class `MyFirstClass`?

x = "MyFirstClass"

- What is instantiation?

creating a new object, and the object is an instance of the class

- What are attributes?

one of the named values associated with an object

- What does it mean when an object is embedded?

an object that is an attribute of another object

- What is the difference between `copy.copy` and `copy.deepcopy`?
What do they each do?

copy.copy aka shallow copy, copies the obbject and any references but not any embedded objects.

copy.deepcopy aka deep copy, will copy the object, objects they refer too, and embedded objects.


- What is the difference between a pure function and a modifier?

A pure function does not modify any of the objects passed to itas arguments and it has no effect, like displaying a value or getting user input, other than returning a value.

A modfier modifies objects as they get passed through parameters.


- What is object-oriented programming?

Programs include class and method definitions

most of the computation is expressed in terms of operations on objects

object ofter represent things in the real world, and methods often correspond to the ways things in the real world interact

## Methods

- What is a method?

a method is a function that is associated with a particular class

- How is a method different than a function?

methods are defined inside of a class

the syntax for invoking a method is different from the syntax of calling a function

- What is invocation?

the act on invoking a funtion

- What is the `__init__` method and what is it used for?

__init__ is a special method that gets invoked when the object is instantiated. It is used as a template to build out objects.

- Give an example `__init__` method for a `Car` class with attributes:
`make`, `model` and `year`.

class Car():

    def__init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

- How do `__init__` methods handle variable arguments?

That's what python's __init__() method is used for. If defined for a class, it gets called right when the instance is created and assigns instance variables, that are defined in there and passed as arguments to the constructor. Let's look at an example of defining the Point() class with such a constructor.


- What is the `__str__` method used for?

returns a string representation of an object

- How do you use a `__str__` method?

 def __str__(self):
        return f"{self.animal_type} | {self.way_of_moving}"


- What is operator overloading?

changing the behavior of an operator so that it works with programmer-defined types

- What is an example of operator overloading?




## TYPE-BASED DISPATCH?

- What is polymorphism?

Polymorphism (meaning "many forms") is the quality that allows one interface to access a general class of action

- Why is polymorphism beneficial?

you can reuse it so you arent writing addiitonal code.
