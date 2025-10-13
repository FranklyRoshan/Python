class Planet:
    # Constructor
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

earth = Planet("Earth", 20000)
print(earth.name)
print(earth.speed)

mars = Planet("Mars", 30000)
print(mars.name)
print(mars.speed)

""""
# Monkey Patching (Dynamic Attribute Assignment)
class Planet: pass

earth = Planet()
mars = Planet()


''' Adding attributes to an object dynamically outside the class definition is called 
    dynamic attribute assignment in Python.

    Unlike Java, Python allows this because it’s a dynamically typed language — 
    you can add or modify attributes at runtime.
    
    This is not allowed in Java without declaring the field or using reflection 
    (and even then, not on a per-instance basis like Python).   '''

earth.name = "Earth"
earth.speed = "20000"
print(earth.name)
print(earth.speed)


# print(mars.name)  

    🔍 Summary:
    Term	                        Meaning
    Dynamic Attribute Assignment	Adding new attributes to objects at runtime.
    Monkey Patching	                Modifying or extending existing classes/objects at runtime.
    Not recommended because	        It breaks encapsulation and maintainability.    """

""" class Planet {
        // Attributes (fields)
        String name;
        int speed;

        // Constructor
        Planet(String name, int speed) {
            this.name = name;
            this.speed = speed;
        }

        // Method to display planet details
        void display() {
            System.out.println(name);
            System.out.println(speed);
        }

        public static void main(String[] args) {
            Planet earth = new Planet("Earth", 20000);
            earth.display();

            Planet mars = new Planet("Mars", 30000);
            mars.display();
        }
    }   """