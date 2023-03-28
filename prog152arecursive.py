import sys
sys.setrecursionlimit(5000)

def add(n):
  if n == 3: return n
  return n + add(n-1)

def main():
  num = int(input("Enter a number: "))
  while num != 0:
    addn = add(num)
    print(f"{num}! = {addn}")
    num = int(input("Enter a number: "))


if __name__ == "__main__":
  main()
    