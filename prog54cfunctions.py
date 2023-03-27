def calcRad(diameter):
  return diameter / 2

def calcArea(diameter, radius):
  radius = calcRad(diameter)
  return 3.14 * radius**2

def calcCirc(diameter, radius):
  return diameter * 3.14

def final(diameter, radius, circumference, area):
  radius = calcRad(diameter)
  area = calcArea(diameter, radius)
  circumference = calcCirc(diameter, radius)
  return radius, area, circumference
  

def main():
  diameter = int(input("What is the Diameter? "))
  r, a, c = final(diameter, radius, circumference, area)
  print(f"Radius: {r}\n Area: {a}\n Circumference: {c}")

if __name__ == "__main__":
  main()