'''
Docstring for creational.singleton

Singleton:
  is a creational design pattern that lets you ensure that a class has only one instance,
  while providing a global access point to this instance
'''

class Singleton:
  _instance = None
  
  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance


if __name__ == "__main__":
  a = Singleton()
  b = Singleton()
  
  print(a is b)
