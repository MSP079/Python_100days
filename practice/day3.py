# Control statements

# if else statement templet

water_level = 50
if water_level >80:
    print("Drain water")
else:
    print("Continue")

print("Welcome to the roller coster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the roller coaster.")
else:
    print("Sorry you have to grow taller before you can ride.")

# =(Assignment) ==(Check equality)

# Modulo operator

print(10%3) # gives remainder 1 has a result

# check Odd or Even
print("Check the even or odd number")
number_to_check = int(input("What is the number you want to check"))
if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")

# Nested if /else if
print("welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >=120:
    print("You can ride the rollercoaster")
    age = int(input("What is you age?"))
    if age <=12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride")


# Multiple if's
print("welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >=120:
    print("You can ride the rollercoaster")
    age = int(input("What is you age?"))
    if age <=12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adults tickets are $12.")
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No")
    if wants_photo == "y":
        #Add $3 to their bill
        bill +=3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride")
