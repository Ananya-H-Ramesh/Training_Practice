import logging

logging.basicConfig(level=logging.INFO,
                    format = "%(levelname)s %(message)s"
                    )


class MyClass:
    x=5
    
p1 = MyClass()
logging.info(p1.x)

#------------__init__() Method

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Ananya",21)
logging.info(p1.name)
logging.info(p1.age)
logging.info(p1)

#--------------__str__() Method

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}({self.age})'


p1 = Person("Ananya",21)
logging.info(p1)

#-----------Object Methods

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def namefunc(self):
        logging.info("Name : "+self.name)


p1 = Person("Ananya",21)
p1.namefunc()

#-----Pass Statement#
#The pass statement is used as a placeholder for future code. 
#When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.

class Person:
    pass





