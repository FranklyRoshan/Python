from abc import ABC, abstractmethod

class AbstractRecipe(ABC): # ABC - Abstract Base Class

    def execute(self):
        self.get_ready()
        self.do_the_dish()
        self.cleanup()

    @abstractmethod
    def get_ready():
        pass

    @abstractmethod
    def do_the_dish():
        pass

    @abstractmethod
    def cleanup():
        pass

class Recipe(AbstractRecipe):

    def get_ready(self):
        print("Get raw material.")
        print("Get Utensils.")
    
    def do_the_dish(self):
        print("Do the dishes.")
    
    def cleanup(self):
        print("Clean Up.")

class RecipeWithMicroWave(AbstractRecipe):

    def get_ready(self):
        print("Get raw materials.")
        print("Switch on the microwave.")

    def do_the_dish(self):
        print("Get stuff ready.")
        print("Put it in the microwave.")

    def cleanup(self):
        print("Cleanup the utensils.")
        print("Switch off the microwave.")        

# TypeError: Can't instantiate abstract class AbstractRecipe without an implementation for abstract methods 'cleanup', 'do_the_dish', 'get_ready'
recipe1 = Recipe()
recipe1.execute()

recipe2 = RecipeWithMicroWave()
recipe2.execute()