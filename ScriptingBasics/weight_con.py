# -*- coding:utf -8 -*-
#!/usr/bin/python3


metric_mass=["'kg', 'g'"]
imperial_mass=["'lb', 'oz'"]

#this defines variables from metric to imperial in mass

def kg_lb(mass):
    print(mass*2.2, "pounds")
def g_oz(mass):
    print(mass*0.035, "ounces")
 #this defines variables from imperial to metric in mass
def lb_kg(mass):
    print(mass*0.4536, "kilograms")
def oz_g(mass):
    print(mass*28.35, "grams")

menu=['1:kg_lb', '2:g_oz', '3:lb_kg', '4:oz_g']
print(menu)
choice = int(input('make your choice:'))
if choice in [1,2,3,4]:
    print('Good')
    mass = int(input('Enter weight to convert:'))
	
if choice == 1:
    print(kg_lb(mass))
elif choice == 2:
    print(g_oz(mass))
elif choice == 3:
    print(lb_kg(mass))
elif choice == 4:
    print(oz_g(mass))
else:
    print("Something went wrong!")


