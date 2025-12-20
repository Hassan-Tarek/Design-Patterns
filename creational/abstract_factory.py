'''
Docstring for creational.abstract_factory

Abstract Factory: 
  is a creational design pattern that let you produce 
  families of related objects without specifying there concrete classes.
'''
from __future__ import annotations
from abc import ABC, abstractmethod

class GUIFactory(ABC):
  '''Abstract Factory: GUIFactory'''
  @abstractmethod
  def create_button(self) -> Button:
    pass
  
  @abstractmethod
  def create_checkbox(self) -> Checkbox:
    pass
  
  
class WindowsFactory(GUIFactory):
  '''Concrete Factory: WindowsFactory'''
  def create_button(self) -> Button:
    return WindowsButton()
  
  def create_checkbox(self) -> Checkbox:
    return WindowsCheckbox()
  
class MacFactory(GUIFactory):
  '''Concrete Factory: MacFactory'''
  def create_button(self) -> Button:
    return MacButton()
  
  def create_checkbox(self) -> Checkbox:
    return MacCheckbox()
  
class LinuxFactory(GUIFactory):
  '''Concrete Factory: LinuxFactory'''
  def create_button(self) -> Button:
    return LinuxButton()
  
  def create_checkbox(self) -> Checkbox:
    return LinuxCheckbox()


class Button(ABC):
  '''Abstract Product: Button'''
  @abstractmethod
  def paint(self) -> str:
    pass

  
class WindowsButton(Button):
  '''Concrete Product: WindowsButton'''
  def paint(self) -> str:
    return "[Windows]: Painting a button in windows platform."
  
class MacButton(Button):
  '''Concrete Product: MacButton'''
  def paint(self) -> str:
    return "[Mac]: Painting a button in mac platform."
  
class LinuxButton(Button):
  '''Concrete Product: LinuxButton'''
  def paint(self) -> str:
    return "[Linux]: Painting a button in linux platform."
  

class Checkbox(ABC):
  '''Abstract Product: Checkbox'''
  @abstractmethod
  def paint(self) -> str:
    pass

  
class WindowsCheckbox(Checkbox):
  '''Concrete Product: WindowsCheckbox'''
  def paint(self) -> str:
    return "[Windows]: Painting a checkbox in windows platform."
  
class MacCheckbox(Checkbox):
  '''Concrete Product: MacCheckbox'''
  def paint(self) -> str:
    return "[Mac]: Painting a checkbox in mac platform."
  
class LinuxCheckbox(Checkbox):
  '''Concrete Product: LinuxCheckbox'''
  def paint(self) -> str:
    return "[Linux]: Painting a checkbox in linux platform."
  
def client_code(gui_factory: GUIFactory):
  '''Client code'''
  button = gui_factory.create_button()
  checkbox = gui_factory.create_checkbox()
  
  print(button.paint())
  print(checkbox.paint())
  
if __name__ == "__main__":
  # Windows factory
  client_code(WindowsFactory())
  
  # Mac factory
  client_code(MacFactory())
  
  # Linux factory
  client_code(LinuxFactory())
