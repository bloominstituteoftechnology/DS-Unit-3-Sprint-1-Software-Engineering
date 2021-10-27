class Vehicle:
    # attributes that will initially be the same for all objects
    wheels = 4

    # constructor
    def __init__(self, make, model, year, mileage, color):
        # initial values of the attributes
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.color = color

    # instance method
    def honk(self):
        print("HOOONK!!!")


# A car class is more specific, so it may have more attributes or at least more specific attributes
# than its parent class
# a car will have all of the attributes of its parent class, plus one new attribute "style"
# class Car:
#     def __init__(self, make, model, year, mileage, color, style):
#         # initial values of the attributes
#         self.make = make
#         self.model = model
#         self.year = year
#         self.mileage = mileage
#         self.color = color
#         self.style = style

#     # instance method
#     def honk(self):
#         print("HOOONK!!!")

#     def description(self):
#         print("I am a", self.make, self.model, "with", self.mileage, "miles. I am a", self.color, self.style, '.')


# If we don't add anything to the car class or override anything from the parent class, then a
# car is just a vehicle, it's as simple as that.
# class Car(Vehicle):
#     super


# A car class is more specific, so it may have more attributes or at least more specific attributes
# than its parent class
# a car will have all of the attributes of its parent class, plus one new attribute "style"
class Car(Vehicle):
    def __init__(self, make, model, year, mileage, color, style):
        # give the Car all of the Vehicle properties
        super().__init__(make, model, year, mileage, color)
        # pluse a new attribute that only applies to cars
        self.style = style

    # We can also give our class new methods that don't exist on the vehicle class
    def description(self):
        print("I am a", self.make, self.model, "with", self.mileage, "miles. I am a", self.color, self.style + '.')