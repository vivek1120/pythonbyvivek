class Car:
    def __init__(self,make, model, year, color,break_iron):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = True
        self.break_iron = break_iron

    def start_engine(self):
        if self.is_running:
            self.is_running = True
            print(f"The {self.make} {self.model}'s engine is now running.")
        else:
            print("The engine is already running.")
        

    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.make} {self.model}'s engine is now off.")
        else:
            print("The engine is already off.")

    def honk(self):
        print(f"The {self.make} {self.model} goes 'Honk Honk!'")

    def get_details(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}, Running: {self.is_running}"

# Usage

toyoto = Car.start_engine

