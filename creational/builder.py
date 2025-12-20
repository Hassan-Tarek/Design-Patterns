'''
Docstring for creational.builder

Builder: 
  is a creational design pattern that let you 
  construct complex objects step by step.
  
This pattern allows to produce different types and representations 
of an object using the same construction code;
'''
from __future__ import annotations
from abc import ABC, abstractmethod

class Computer:
  
  def __init__(self):
    self.cpu = None
    self.ram = None
    self.storage = None
    self.gpu = None
  
  def __str__(self) -> str:
    return (
      f"Computer("
      f"CPU={self.cpu}, "
      f"RAM={self.ram}, "
      f"Storage={self.storage}, "
      f"GPU={self.gpu})"
    )


class ComputerBuilder(ABC):
  
  @abstractmethod
  def add_cpu(self):
    pass

  @abstractmethod
  def add_ram(self):
    pass

  @abstractmethod
  def add_storage(self):
    pass

  @abstractmethod
  def add_gpu(self):
    pass

  @abstractmethod
  def get_result(self):
    pass

class GamingComputerBuilder(ComputerBuilder):
  
  def __init__(self):
    self.computer = Computer()
  
  def add_cpu(self):
    self.computer.cpu = "Intel Core i9"
    
  def add_ram(self):
    self.computer.ram = "32GB"
  
  def add_storage(self):
    self.computer.storage = "1TB SSD"
    
  def add_gpu(self):
    self.computer.gpu = "RTX 4090"
    
  def get_result(self):
    return self.computer

class PersonalComputerBuilder(ComputerBuilder):
  
  def __init__(self):
    self.computer = Computer()
    
  def add_cpu(self):
    self.computer.cpu = "Intel Core i5"
  
  def add_ram(self):
    self.computer.ram = "16GB"
  
  def add_storage(self):
    self.computer.storage = "512GB SSD"
  
  def add_gpu(self):
    self.computer.gpu = "Integrated Graphics"
    
  def get_result(self) -> Computer:
    return self.computer


class ComputerDirector:
  
  def __init__(self, builder: ComputerBuilder):
    self.builder = builder
  
  def build_computer(self):
    self.builder.add_cpu()
    self.builder.add_ram()
    self.builder.add_storage()
    self.builder.add_gpu()
    return self.builder.get_result()


def client_code(builder: ComputerBuilder):
  director = ComputerDirector(builder)
  computer = director.build_computer()
  print(computer)

if __name__ == "__main__":
  # Gaming computer builder
  gaming_computer_builder = GamingComputerBuilder()
  client_code(gaming_computer_builder)
  
  # Personal computer builder
  personal_computer_builder = PersonalComputerBuilder()
  client_code(personal_computer_builder)
