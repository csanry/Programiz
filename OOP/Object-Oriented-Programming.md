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

- In the above program, we created a class with the name `Parrot`. 

- Then, we defined attributes. The attributes are a characteristic of an object.

- These attributes are defined inside the `__init__()` method of the class. 

- It is the constructor method that is run as soon as the object is created.

- We can access the class attribute using `__class__.species`. 

- Class attributes are the same for all instances of a class. 

- Similarly, we access the instance attributes using `tweety.name` and `tweety.age`. 

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
---

#### Inheritance

- Inheritance is a way of creating a new class for using details of an existing class without modifying it. 

- The newly formed class is a derived class (or child class). 

- Similarly, the existing class is a base class (or parent class).

```python
# parent class
class Bird: 
    def __init__(self):
        print('Bird is ready')
    def who_is_this(self):
        print('Bird')
    def swim(self):
        print('Swim faster')
    
# child class 
class Penguin(Bird):
    def __init__(self):
        # call super() function to call the Parent
        super().__init__()
        print('Penguin is ready')
    # modifies the parent method
    def who_is_this(self):
        print('Penguin')
    def run(self):
        print('Run faster')

peggy = Penguin()
peggy.who_is_this()
peggy.swim()
peggy.run()
```

```
Bird is ready
Penguin is ready
Penguin
Swim faster
Run faster
```

---

#### Encapsulation

- We can restrict access to methods and variables. 

- This prevents data from direct modification which is called encapsulation.

- We denote private attributes using underscores as the prefix i.e single `_` or double `__`. This is by convention.

```python
class Computer:
    def __init__(self):
        self.__maxprice = 900
    
    def sell(self):
        print(f'Selling Price: {self.__maxprice}')
    
    def set_max_price(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.set_max_price(1000)
c.sell()
```

```
Selling Price: 900
Selling Price: 900
Selling Price: 1000
```

- In the above program, we defined a `Computer` class

- self.__maxprice can't be modified using assignment.

- To modify the function, we need to use a setter function.

---


#### Polymorphism

Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.

```python
class Parrot:
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("Penguin can't fly")
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
```

```
Parrot can fly
Penguin can't fly
```

- In the above program, we defined two classes `Parrot` and `Penguin`. 

- Each of them have a common `fly()` method. However, their functions are different.

- To use polymorphism, we created a common interface i.e `flying_test()` function that takes any object and calls the object's `fly()` method.

- Thus, when we passed the `blu` and `peggy` objects in the `flying_test()` function, it ran effectively.

---


- Object-Oriented Programming makes the program easy to understand as well as efficient.

- Since the class is sharable, the code can be reused.

- Data is safe and secure with data abstraction.

- Polymorphism allows the same interface for different objects, so programmers can write efficient code.




**TO BE CONTINUED >>** 







