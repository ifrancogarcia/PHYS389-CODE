import math

'''The class Isotope defines teh properties of an isotope such as its decay rate, 
it's final quantity, its half-life, etc. Different fucntions describe each quantity.

The program uses math module, which will facilitate the calculations.'''

class Isotope:

    '''The __init__ functionis called every time an object is created from a class.'''

    def __init__(self,
                initial_quantity,
                decay_constant):
        
        #self.name = name
        self.initial_quantity = initial_quantity
        self.decay_constant = decay_constant
        #self.half_life = math.log(2.0)/decay_constant
        #self.time = 0.1*self.half_life #why 0.01???

    def final_quantity(self, time):
        quantity = self.initial_quantity * math.exp(-self.decay_constant * time)
        return quantity

    def decay_rate(self, quantity):
        rate = -self.decay_constant * quantity
        return rate
    
#EXAMPLE
'''Below is a test with arbitrary numbers to test that teh functions are calculating properly.'''
initial_quantity = 100
decay_constant = 3
time = 10

isotope = Isotope(initial_quantity, decay_constant)
final_quantity = isotope.final_quantity(time)
decay_rate = isotope.decay_rate(final_quantity)

print("Final Quantity:", final_quantity)
print("Decay Rate:", decay_rate)