class MotorBike:
    
    def __init__(self, gear,speed):
        self.gear = gear
        self.speed = speed
    

    def __repr__(self):
        return repr((self.gear, self.speed))
    
    # instance methods.
    def gear_shift(self, which_gear):
        self.gear = which_gear
    
    def increase_speed(self, how_much):
        self.speed += how_much

    def decrease_speed(self, how_much):
        self.speed -= how_much


# instance 1 or object 1
bike1 = MotorBike(1, 10)
# instance 2 or object 2
bike2 = MotorBike(2, 20)
# instance 3 or object 3
bike3 = MotorBike(3, 30)

# instance 4 or object 4
bike4 = MotorBike(4, 40)
bike4.gear_shift(5)
bike4.increase_speed(50)

print(bike1)
print(bike2)
print(bike3)
print(bike4)