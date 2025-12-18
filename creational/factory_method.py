'''
Docstring for creational.factory_method

Factory Method: 
  is a creational design pattern that provides an interface for 
  creating objects in a superclass, but allow subclasses to 
  alter the type of objects that wil be created.

'''
from __future__ import annotations
from abc import ABC, abstractmethod

class Dialog(ABC):
  
  @abstractmethod
  def create_button(self) -> Button:
    """Dialog Factory Method"""
    raise NotImplementedError("You must implement create_button() method.")
  
  def render_window(self):
    button = self.create_button()
    
    print(f"Dialog: Drawing window layout...")
    print(button.render())
    print(button.on_click())


class WindowsDialog(Dialog):
  
  def create_button(self) -> Button:
    return WindowsButton()

class MacDialog(Dialog):
  
  def create_button(self) -> Button:
    return MacButton()

class LinuxDialog(Dialog):
  
  def create_button(self) -> Button:
    return LinuxButton()


class Button(ABC):
  
  @abstractmethod
  def render(self) -> str:
    '''Button Factory Method'''
    raise NotImplementedError("you must implement render() method.")
  
  @abstractmethod
  def on_click(self) -> str:
    '''Button Factory Method'''
    raise NotImplementedError("you must implement on_click() method.")

  
class WindowsButton(Button):
  
  def render(self) -> str:
    return "[Windows]: Rendering a button in windows platform."
  
  def on_click(self) -> str:
    return "[Windows]: Click event triggered."
  
class MacButton(Button):
  
  def render(self) -> str:
    return "[Mac]: Rendering a button in mac platform."
  
  def on_click(self) -> str:
    return "[Mac]: Click event triggered."
  
class LinuxButton(Button):
  
  def render(self) -> str:
    return "[Linux]: Rendering a button in linux platform."
  
  def on_click(self) -> str:
    return "[Linux]: Click event triggered."
  
  
def client_code(dialog: Dialog):
  dialog.render_window()
  
if __name__ == "__main__":
  # Windows dialog
  client_code(WindowsDialog())
  
  # Mac dialog
  client_code(MacDialog())
  
  # Linux dialog
  client_code(LinuxDialog())
  