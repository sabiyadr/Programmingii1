def calcRad(diameter):
  return diameter / 2

def calcArea(diameter, radius):
  radius = calcRad(diameter)
  return 3.14 * radius**2

def calcCirc(diameter, radius, circumference):
  return diameter * 3.14

def final(radius, circumference, area):
  radius = calcRad(diameter)
  circumference = calcCirc(diameter, radius, circumference)
  area = calcArea(diameter, radius)
  return radius, area, circumference
  

def main():
  diameter = int(input("What is the Diameter? "))
  r, a, c = final(radius, circumference, area)
  print(f"Radius: {r}\n Area: {a}\n Circumference: {c}")

if __name__ == "__main__":
  main()