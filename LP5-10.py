num1 = int(input("Enter First Number: "))
num2 = int(input("Enter a Second Number: "))

while num2 > 0:
  temp = num1 % num2
  num1 = num2
  num2 = temp

print("The GCD is ", num1)