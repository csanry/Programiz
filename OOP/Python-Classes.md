## This section covers the core functionality of Python objects and classes.

---

#### Defining a class in Python 

- Class definitions begin with a `class` keyword - classes are blueprints that contain details on how to build objects.

- The first string inside the class is a `docstring` and is denoted with three apostrophes. 

```python
# Simple class definition 
class MyNewClass:
    '''This is a docstring'''
    pass
```

- There are many special attributes that begin with double underscores `__`. To view a full list, enter `dir(MyClass)`.


---

#### Creating an Object in Python 

```python
harry = Person()
```

- This will create a new object instance named `harry`. We can access the attributes using dot notation.

```python
class Person:
    '''
    This is a person class
    '''
    age = 10
    
    def greet(self):
        print('Hello')

harry = Person()
print(harry.greet()) # Output: Hello
```

- Whenever an object calls its method, the object itself is passed as the first argument.

- `harry.greet()` translates into `Person.greet(harry)`

- Therefore, the first argument of a method must be the object itself. This is conventionally called `self`.

---

#### Constructors in Python 

- A constructor is a special function that gets called whenever a new object of that class is instantiated.

- In Python, this is the `__init__()` function, which is normally used to initialize all the variables.

```python
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')
```

- Whenever an object calls its method, the object itself is passed as the first argument.

- `harry.greet()` translates into `Person.greet(harry)`

- Therefore, the first argument of a method must be the object itself. This is conventionally called `self`.

---

#### Creating and deleting attributes 



**TO BE CONTINUED >>** 







