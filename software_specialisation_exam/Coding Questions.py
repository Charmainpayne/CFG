# CODING QUESTIONS 

# SECTION 2
     
# 2.1

def count_unique_consonants(string):
    #returns the number of unique consonants in the given string
    
    # Define a set of vowels
    vowels = set('aeiou')
    
    # Create an empty set to store unique consonants
    unique_consonants = set()
    
    # Iterate through each character in the string
    for char in string.lower():
        # Check if the character is a consonant
        if char.isalpha() and char not in vowels:
            unique_consonants.add(char)
    
    # Return the length of the set of unique consonants
    return len(unique_consonants)

# 2.2
       
    #The time complexity of this algorithm is O(n) because it iterates through the string once.
    #The space complexity is O(n) because it creates a set to store the unique consonants.
    
    #My assumptions - The input string contains only alphabetic characters (letters) and spaces.
    #Uppercase and lowercase letters are considered the same for the purpose of counting unique consonants.


#2.3

def count_squares(n):
    #returns the number of squares in an n x n grid
  
    # Base case: If n is 0, there are no squares
    if n == 0:
        return 0
    
    # Recursive: Calculate the number of squares of size n
    # and add it to the number of squares in the (n-1) x (n-1) grid
    return n * n + count_squares(n - 1)

# THEORY CHALLENGE
# 
# SECTION 3

# 3.1

# To design a hash function using ASCII codes, see the following example:
# I have a hash table of size 5 and i want to insert the following key values: 
# ("apple", 1), ("banana", 2), ("cherry", 3), ("date", 4), and ("elderberry", 5)
# 1 - Calculate the index for "apple" using the hash function. It maps to index 2.
# 2 - Create the a new node with the key-value pair ("apple", 1) and add it to the linked list at index 2.
# 3 - Calculate the index for "banana" using the hash function. It also maps to index 2.
# 4 - Since the linked list at index 2 is not empty, I create a new node with the key-value pair ("banana", 2) and append it to the end of the linked list at index 2.
# 5 - Repeat this process for the remaining key-value pairs.

#3.2

# This function takes the name of the item and converts each character to its ASCII code
# and adds them up to calculate the hash value. The hash value is returned.
# This produces a number between 0 - 9
# I have a small bookshelf with 10 shelves and i want to store items in these shelves based on their titles.

# For the item "apple Pie":
# I convert each character to its ASCII code and add them up: 65 + 112 + 112 + 108 + 101 + 32 + 80 + 105 + 101 = 814.
# I take 814 modulo 10 (the number of storage units), which gives us 4.
# Since storage unit 4 is empty, we place the item "apple" with its value 1 in storage unit 4.

# i continue with the same process for the other items ("apple", 1), ("banana", 2), ("cherry", 3), ("date", 4), and ("elderberry", 5)
# In this example, there is a hash collision when we try to insert the item "date" 
# because it maps to the same storage unit (4) as the item "apple". To handle this collision, we can use a technique called separate 
# chaining, where we store a linked list of items at each storage unit.

# 3.3

# This function takes the name of the item and converts each character to its ASCII code
# and adds them up to calculate the hash value. The hash value is returned.
# This produces a number between 0 - 9
# I have a small storage facility with 10 units and i want to store items in these units based on their names.

# For the item "apple":
# I convert each character to its ASCII code and add them up: 97 + 112 + 112 + 108 + 101 = 534.
# I take 534 modulo 10 (the number of storage units), which gives us 4.
# Since storage unit 4 is empty, we place the item "apple" with its value 1 in storage unit 4.

# i continue with the same process for the other items ("apple", 1), ("banana", 2), ("cherry", 3), ("date", 4), and ("elderberry", 5)
# In this example, there is a hash collision when we try to insert the item "date" 
# because it maps to the same storage unit (4) as the item "apple". To handle this collision, we can use a technique called separate 
# chaining, where we store a linked list of items at each storage unit.

# CODING CHALLENGE

# SECTION 4

# 4.1
# 25 MARKS
"""
A] Design a parent class called Planet

It must have:
- General attributes: name, distance_from_sun, planet_type
- A get_distance_to_earth() method that gives you the absolute distance from the Earth.

!!! You can take the distance from the Sun to the Earth as 147 million kilometres !!!

For example, if the planet’s distance_from_sun was 148 million kilometres when you call the get_distance_from_earth()
method, it should give us the distance like this: {'distance to earth’': 1000000} where the implied unit is kilometres.
This means that the planet is 1 million kilometres away from Earth.

   > This question uses an oversimplification of the solar system model, not taking into account orbit position or the
    eccentricity of the orbit, so in reality the result will be an approximate value with a reasonable margin of error.
"""

class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        #initialize a plant object with a name, distance from the Sun, and planet type
        
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def get_distance_to_earth(self):
        
        """
        Calculate the absolute distance of the planet from Earth in kilometers.

        Returns:
            dict: A dictionary containing the distance to Earth in kilometers.
        """
        earth_distance_from_sun = 147  # Distance from the Sun to Earth in millions of kilometers
        distance_to_earth = abs(self.distance_from_sun - earth_distance_from_sun)
        return {'distance to earth': distance_to_earth * 1000000}  # Convert to kilometers


"""
B] Design a child class called Mercury, which inherits from the Planet class.
This class should have exactly the same attributes as its parent class,
Your child class should also have a static method called happy_new_year(), which
would give us the information on how long a year lasts on the planet (in whatever way you wish!). 
You can take Earth Days as the implied unit.

After, create a Mercury object and print out the value of all its attributes and methods.

!!! HELPFUL INFO ABOUT MERCURY !!!
Distance from Sun: 58 million
Planet Type: Terrestrial
Time taken for the planet to orbit the sun: 88 Earth days
!!!!!!!!!!!!!!!!!!!!

"""
class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def get_distance_to_earth(self):
        earth_distance_from_sun = 147
        distance_to_earth = abs(self.distance_from_sun - earth_distance_from_sun)
        return {'distance to earth': distance_to_earth * 1000000}

class Mercury(Planet):
    def __init__(self, name, distance_from_sun, planet_type):
        super().__init__(name, distance_from_sun, planet_type)

    @staticmethod
    def happy_new_year():
    
        print("The length of a year on Mercury is 88 Earth days.")
        
# Mercury object with properties
mercury = Mercury("Mercury", 58, "Terrestrial")

# Print the attributes of the Mercury object
print("Name:", mercury.name)
print("Distance from Sun (in millions of km):", mercury.distance_from_sun)
print("Planet Type:", mercury.planet_type)

# Call the get_distance_to_earth() method
mercury_distance_to_earth = mercury.get_distance_to_earth()
print("Distance to Earth (in km):", mercury_distance_to_earth)

# Call the happy_new_year() static method
Mercury.happy_new_year()


"""
C] Design a child class called Jupiter, which inherits from the Planet class.
This class should have exactly the same attributes as its parent class, as well as the additional attribute 
number_of_moons.
Your child class should also have a static method called happy_new_year(), which would give us the information on how 
long a year lasts on the planet (in whatever way you wish!). You can take Earth Days as the implied unit.

After, create a Jupiter object and print out the value of all its attributes and methods.


!!! HELPFUL INFO ABOUT JUPITER !!!
Distance from Sun: 779 million
Planet Type: Gas Giant
Time taken for the planet to orbit the sun: 4383 Earth days
Number of Moons: 80
!!!!!!!!!!!!!!!!!!!!

"""

class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def get_distance_to_earth(self):
        earth_distance_from_sun = 147
        distance_to_earth = abs(self.distance_from_sun - earth_distance_from_sun)
        return {'distance to earth': distance_to_earth * 1000000}

class Jupiter(Planet):
    def __init__(self, name, distance_from_sun, planet_type, number_of_moons):
        super().__init__(name, distance_from_sun, planet_type)
        self.number_of_moons = number_of_moons

    @staticmethod
    def happy_new_year():
      
        print("One year on Jupiter lasts approximately 4383 Earth days!")

# Create a Jupiter object with real-life properties
jupiter = Jupiter("Jupiter", 779, "Gas Giant", 80)

# Print the attributes of the Jupiter object
print("Name:", jupiter.name)
print("Distance from Sun (in millions of km):", jupiter.distance_from_sun)
print("Planet Type:", jupiter.planet_type)
print("Number of Moons:", jupiter.number_of_moons)

# Call the get_distance_to_earth() method
jupiter_distance_to_earth = jupiter.get_distance_to_earth()
print("Distance to Earth (in km):", jupiter_distance_to_earth)

# Call the happy_new_year() static method
Jupiter.happy_new_year()


 