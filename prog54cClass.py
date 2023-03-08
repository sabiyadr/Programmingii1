class Circle:
  def __init__(self, diameter):
    self.diameter = diameter
    self.area = 0
    self.radius = 0
    self.circ = 0

  def solve(self):
    self.radius = self.diameter / 2
    self.area = 3.14 * self.radius**2
    self.circ = self.diameter * 3.14
    
  def gArea(self):
    return self.area
    
  def gRadius(self):
    return self.radius
    
  def gCirc(self):
    return self.circ

def main():
  diameter = int(input("Type the diameter: "))
  circle = Circle(diameter)
  circle.solve()
  print("Radius: ", circle.gRadius())
  print("Area", circle.gArea())
  print("Circumference: ", circle.gCirc())


if __name__ == "__main__":
  main()
  