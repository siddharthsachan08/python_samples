print("welcome to sid's palace")
ddd = input("what would you like to buy pen,pencil,book?")
if(ddd.lower() == "pen"):
  fff = int(input("how much would you like to buy"))
  print("Your bill value is",(fff*2),"dollars")
elif(ddd.lower() == "pencil"):
  sss = int(input("how much would you like to buy"))
  print("Your bill value is",(sss*1),"dollars")
elif(ddd.lower() == "book"):
  ccc = int(input("how much would you like to buy"))
  print("Your bill value is",(ccc*12),"dollars")
else:
  print("sorry we only have book, pen and pencil")