import sys
sys.setrecursionlimit(50000)

def add(n):
  if n == 3: return n
  return n + add(n-1)

def main():
  add(n)

if __name__ == "__main__":
  main()
    