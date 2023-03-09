class CL213F:
  def __init__(self, kwh):
    self.kwh = kwh
    self.cost = 0.0

  def calc(self):
    if self.kwh >= 0 and self.kwh < 8000:
      self.cost = 0.07
    elif self.kwh >= 8000 and self.kwh < 10000:
      self.cost = 0.05
    elif self.kwh >= 10000:
      self.cost = 0.04

      

  def __str__(self):
    return f"The cost of {self.kwh} is {self.cost * self.kwh}"