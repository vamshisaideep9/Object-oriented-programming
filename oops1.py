class Employee:
    def __init__(self):
        print("stated executing data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes and data have been initiated")

    #creating a method
    def travel(self, destination):
        print("This travel method was called manually.")
        print(f"employee is now travelling to {destination}")


#creating an instance of the class
sam = Employee()
sam.travel("kerala")

print(type(sam))
