print(" Welcome to bibi coffee shop...!!!!! ")
name = input(" tapai ko naam k ho ....? \n")
if  name == "ganga" or name== "bibek" or name =="durga":
 evil_status = input("k tapai aasur ho ? ")
 good_deeds = int(input("tapai lea kati ota ramro kam garnu vako xa ? /n"))
 if evil_status == "yes" and good_deeds <4:
  print("Bahira jau kasto khattam manxe " + name + " mero pasal bata jau ani kaile pani na aau this is warmly warning to you ")
  exit()
 else:
  print("oh, kasto ramro  gajmer welcome  dear")
else:
 print("hello " + name + " you are  welcome in our cofee shop")
 #logical operator
 #name = input("what is your name ? ")
print (" hello how are you ? " + name + " thanks for visitng our shop here is our serving list ")
menu = " black coffee, milk tea, hachikano, chimlatte"
print( name + " what would you like to from menu today ? here are our serving list . \n " + menu)
order = input("what you want ? ")
quantity = input(" How many quantity you want ?\n")
if order == "black coffee":
 price =20
elif order == "milk tea":
  price =30
elif order == "hachikano":
 price =50
elif order == "chimlatte":
 price =40
else:
 print("Sorry, we don't have that here hehehe...!")
 exit()

total = int(quantity) * price
print("oh sounds tasty " + name + " we will deliver your order that in a minutes " + order + " enjoy your meal " + " your total amount & bill is " + str(total) + " please pay through esewa or pay in our counter" )

