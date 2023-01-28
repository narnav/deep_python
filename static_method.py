from datetime import date


class Math_samp:
    cls_var = 4

    @staticmethod
    def abs(num1):
        if num1 < 0:
            return num1 * -1
        return num1


print(Math_samp.abs(-3))


# class method

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate age an set it as a age
        # return new object
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))


jessa = Student('Jessa', 20)
jessa.show()

# create new object using the factory method
joy = Student.calculate_age("Joy", 1995)
joy.show()
