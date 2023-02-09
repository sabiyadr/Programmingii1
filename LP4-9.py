import random
pnum = int(input("Enter a Number Between 1 and 20: "))
ainum = random.randint(1, 20)
print("Computers Number: ", ainum)
print("Your Number: ", pnum)
if pnum in range(1, 20):
  if ainum == pnum:
    print("You Won!")
  elif not ainum == pnum:
    print("Better Luck Next Time")
else:
  print("Your Number is Invalid")