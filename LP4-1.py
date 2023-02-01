copies = int(input("Enter number of copies to be printed: "))

if copies > 0 and copies <= 99:
  price = 0.30
elif copies > 99 and copies <= 499:
  price = 0.28
elif copies > 499 and copies <= 749:
  price = 0.26
elif copies >= 1000:
  price = 0.25
else:
  print("Number of copies is invalid")

print("Price Per Copy: $" + str(price))
print("Total Price: $" + str(price*copies))