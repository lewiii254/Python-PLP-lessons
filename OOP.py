class Car:
    # Attributes (properties)
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    # Method (behavior)
    def start(self):
        return f"The {self.color} {self.make} {self.model} starts."

    def stop(self):
        return f"The {self.color} {self.make} {self.model} stops."

# Creating objects (instances) from the Car class
car1 = Car("Toyota", "Corolla", "red")
car2 = Car("Honda", "Civic", "blue")

# Interacting with objects
print(car1.start())  # Output: The red Toyota Corolla starts.
print(car2.stop())   # Output: The blue Honda Civic stops.