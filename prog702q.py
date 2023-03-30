from CL702Q import *

def main():
  try:
    vehicle = []
    with open("data/prog702q.txt", 'r') as f:
      num = int(f.readline())
      while num != 99:
        nm = f.readline()
        ts = int(f.readline())
        if num == 1:
          worth = int(f.readline())
          v = Cars(nm, ts, worth)
          vehicle.append(v)
        elif num == 2:
          miles = float(f.readline())
          v = Trucks(nm, ts, miles)
          vehicle.append(v)
        if num == 3:
          hc = f.readline().strip()
          v = Buses(nm, ts, hc)
          vehicle.append(v)
        num = int(f.readline())

      totw = 0
      totm = 0.0
      home = []

      for Vehicles in vehicle:
        if isinstance(Vehicles, Cars):
          totw += Vehicle.worth
        if isinstance(Vehicles, Trucks):
          totm += Vehicles.miles


    print("Average Cars Worth: ", totw)
    print("Trucks Milage: ", totm)
    print("")

  except Exception as e:
    print("Error: ", e)


if __name__ == "__main__":
  main()