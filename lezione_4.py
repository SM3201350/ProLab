#Definire oggetti
#import the random module
import random
class Person():

    def __init__(self,name,surname):

        #set name and surname
        self.name = name
        self.surname = surname

    def __str__(self):
        return 'Person "{} {}"'.format(self.name,self.surname)

    def say_hi(self):

        #Generate a random number between 0, 1 and 2
        random_number = random.randint(0,2)

        #Choose a random greeting
        if random_number == 0:
            print('Hello, I am {} {}.'.format(self.name,self.surname))
        elif random_number == 1:
            print('Hi, I am {}!'.format(self.name))
        elif random_number == 2:
            print('Yo bro! {} here!'.format(self.name))

#estendere oggetti
class Student(Person):

    def __str__(self):
        return 'Student "{} {}"'.format(self.name,self.surname)



class Professor(Person):

    def __str__(self):
        return 'Prof. "{} {}"'.format(self.name,self.surname)

    def say_hi(self):
        print('Hello, I am professor {} {}.'.format(self.name,self.surname))

    def original_say_hi(self):
        super().say_hi()

        
print('--------------------')

person = Person('Mario','Rossi')

print(person)
person.say_hi()

print('--------------------')

prof = Professor('Pippo','Baudo')

print(prof)
prof.say_hi()
prof.original_say_hi()

print('--------------------')

student = Student('Anna','Di Giovanni')

print(student)
student.say_hi()
