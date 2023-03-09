from CL213F import *

def main():
  try:
    elecbills = []
    with open("data/prog213f.dat", 'r') as f:
      for line in f:
        kwh = float(line.strip())
        if kwh != -999:
          bill = CL213F(kwh)
          elecbills.append(bill)
    for bill in elecbills:
      bill.calc()
      print(bill) # same as print(str(bill))
          

  except Exception as e:
    print("Error: ", e)


if __name__ == "__main__":
  main()
