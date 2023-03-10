import datetime


class Student:
  def __init__(self):
    self.name='saman'
    self.birth_year=2003
    self.height=190
    self.weight=78

  def display(self):
    item = ' '
    item+=f'name : {self.name}\tage : {self.birth_year}\theight : {self.height}\tweight : {self.weight}\n'
    return item
   

  def calculate_age(self):
    current_time =datetime.datetime.now()
    return current_time.year - self.birt h_year