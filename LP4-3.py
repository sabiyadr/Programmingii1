pdozen = 0.0
eggs = int(input("How much dozen off eggs do you want: "))
if eggs <= 3:
  pdozen = 0.50
elif eggs > 3 and eggs <= 5:
  pdozen = 0.45
elif eggs > 5 and eggs <= 10:
  pdozen = 0.40
elif eggs > 11:
  pdozen = 0.35
else:
  print("Invalid Amount")

print("Bill per dozen: ", str(pdozen))
print("Total: ", str(pdozen*eggs))
