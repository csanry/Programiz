## This section covers Object-Oriented Programming (OOP) in Python and its fundamental concepts with the help of examples.

---

#### An object has two characteristics:

- Attributes

- Behavior

#### Using an example:

A parrot is an object as it has the following properties:

- Name, age, colour as attributes.

- Squawking, repeating as behaviors.

---

#### Python Class

- A class is a blueprint for the object.

- We can think of a class as a sketch of a parrot with labels - it contains descriptions 
of attributes such as the name, colors, size etc. 

- We can define the simplest class using:

```python
class Parrot: 
    pass

# Instantiate an object of class Parrot
birdy = Parrot()
```

---

#### Building on the class

- We can add more details on parrots by building on the class.

```python
class Parrot:
    # class attribute
    species = 'bird'

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate an object of class Parrot with the attributes
tweety = Parrot('Blu', 2)

# Access class level attributes: bird
print(tweety.__class__.species)
# Access instance attributes: Blu 
print(tweety.name)
```

- In the above program, we created a class with the name Parrot. 

- Then, we defined attributes. The attributes are a characteristic of an object.

- These attributes are defined inside the __init__ method of the class. 

- It is the initializer method that is first run as soon as the object is created.

- Then, we create instances of the Parrot class (Tweety). 

- We can access the class attribute using __class__.species. 

- Class attributes are the same for all instances of a class. 

- Similarly, we access the instance attributes using tweety.name and tweety.age. 

- Instance attributes are different for every instance of a class.

---

#### Methods

- Methods are functions defined inside the body of a class. 

- They are used to define the behaviours of an object.

```python
class Parrot: 
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return f"{self.name} sings {song}"

    def dance(self):
        return f"{self.name} is now dancing"

# instantiate the object 
blu = Parrot('Blu', 2)

# call our instance methods sing: Blu sings 'Happy' 
print(blu.sing("'Happy'"))
# Blu is now dancing
print(blu.dance())
```


**TO BE CONTINUED >>** 






