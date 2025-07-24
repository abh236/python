# simple class with methods and constructor
'''class animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."
Animal= animal("Generic Animal")
print(Animal.name,Animal.speak())'''

# simple class with instance variables and methods
'''class animal:
    animal_count = 0  
    def __init__(self, name):
        self.name = name
        animal.animal_count += 1

    def speak(self):
        return f"{self.name} makes a sound."
Animal= animal("Generic Animal")
Animal2 = animal("Dog")
animal3 = animal("Cat")
print(f"Total Animal:{animal.animal_count}")  

print(Animal.name)
print(Animal2.name)
print(animal3.name)'''


# class with inheritance with both multiple and multi-level inheritance and use of super()
'''class vehicle:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")
class fuel_vehicle(): 
  def fuel(self, fuel):
    self.fuel = fuel
    print(f"Fuel type: {self.fuel}")
    
  def display_fuel(self):
    print(f"Fuel type: {self.fuel}")  
class car(vehicle, fuel_vehicle):
  
  def __init__(self, brand, model, year,name):
    super().__init__(brand, model, year)
    self.name = name  
    

  

  
  def display_info(self):
    print(f"name: {self.name}")
    super().display_info()



       
class bike(vehicle,fuel_vehicle):
  
  def __init__(self, brand, model, year,name):
    super().__init__(brand, model, year)
    self.name = name
    
  
  
  def display_info(self):
    print(f"name: {self.name}")
    super().display_info()

  

bike1 = bike(f"Yamaha", "FZ", 2020,"Bike1")
car1 = car("Toyota", "Corolla", 2021,"Car1")
bike1.display_info()
bike1.fuel("Petrol")
car1.display_info()
car1.fuel("Diesel")'''

# polymorphism 
 # with inheritance
'''from abc import ABC, abstractmethod
class shape:
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(f"Circle area: {3.14 * self.radius * self.radius}")
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print(f"Rectangle area: {self.length * self.breadth}")
class square(shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        print(f"Square area: {self.side * self.side}")                    
class pizza(circle):
    def __init__(self, radius):
        self.radius = radius
   
shapes = [circle(5), rectangle(4, 6), square(3), pizza(7)]   
for shape in shapes:
    shape.area()'''

  # with ducket methods  
'''class shape:
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(f"Circle area: {3.14 * self.radius * self.radius}")
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print(f"Rectangle area: {self.length * self.breadth}")
class square(shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        print(f"Square area: {self.side * self.side}")                    
class pizza:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(f"Pizza area: {3.14 * self.radius * self.radius}")    
   
shapes = [circle(5), rectangle(4, 6), square(3), pizza(7)]   
for shape in shapes:
    shape.area()  '''

# static and class methods
'''class employee:
    employee_count = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        employee.employee_count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    @staticmethod
    def is_adult(age):
        return age >= 18
    
print(employee.is_adult(20)) 
print(employee.is_adult(16))  
employee1 = employee('abhi',18)
employee2 = employee('xyz',20)
print(employee.get_employee_count())  
employee3 = employee('pqr',17)
print(employee1.name,employee1.age) 
print(employee2.name,employee2.age)
print(employee3.name,employee3.age)  
print(employee2.is_adult(employee2.age))'''

# Magic methods-use of double underscore methods
'''class book:
    def __init__(self, title, author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        if isinstance(other, book):
            return self.title == other.title and self.author == other.author
        return False
    def __lt__(self, other):
        if isinstance(other, book):
            return self.pages < other.pages
        return False
    def __gt__(self, other):
        if isinstance(other, book):
            return self.pages > other.pages
        return False
    def __add__(self, other):
        if isinstance(other, book):
            return self.pages + other.pages
        return NotImplemented
    def __contains__(self, keyword):
        return keyword.lower() in self.title.lower() or keyword.lower() in self.author.lower()
    def __getitem__(self,key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'pages':
            return self.pages
        else:
            raise KeyError(f"Invalid key: {key}")


book1 = book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = book("1984", "George Orwell", 328)
print(book1) 
print(book2==book3)
print(book1 < book2)
print(book1 > book2)
print(book1 + book2)
print("Gatsby" in book1)
print(book1['title'])
print(book1['author'])
print(book1['pages'])'''

# property decorator
'''class person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError("Age must be a non-negative integer.")
    @age.deleter
    def age(self):
        print("Deleting age...")
        del self._age
    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name

person1 = person("Alice", 30)
print(person1.name)
print(person1.age)
person1.name = "Bob"
print(person1.name)
person1.age = 85
print(person1.age)
del person1.age
del person1.name'''

