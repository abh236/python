# property decorator with docstrings
'''def my_property(func):
  def wrapper( *args, **kwargs):
    print(f"Getting {func.__name__}")
    func( *args, **kwargs)
  return wrapper
  
def my_property2(func):
  def wrapper( *args, **kwargs):
    print(f"Setting {func.__name__}")
    func( *args, **kwargs)
  return wrapper
  
@my_property
@my_property2
def name( value):
  print(f"hi {value}")

name("a87")  '''

# exceptoin handling


'''try :
  a=1
  b=int(input("enter a number"))
  print(a/b)

except ZeroDivisionError:
  print("you can't divide by zero")

except ValueError:
  print("you didn't enter a number")

except Exception:
  print("something went wrong")

finally:
  print("this will always run")'''

strs = "flower flow3flight "


strs=strs.replace("r", "")
print(strs)