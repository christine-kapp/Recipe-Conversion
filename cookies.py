# chocolate chip cookie recipe ingredient conversion


print("Hi! Welcome to the Recipe Ingredient Conversion Tool.")
print("ei Your personal calculator for altering recipes without the hastle.")
print()

print("The recipe we will be looking at today bakes 5 dozen chocolate chip cookies!")
print("This calculator will allow for you to modify the amount of cookies baked.")
print()

dozens = int(input("Enter how many dozens you would like to bake: "))
print("You have selected:",dozens,"dozen")
print()


original = 5   # number of dozens original recipe makes


# flour

print("The original recipe calls for 2.25 cups of flour.")
print()

flour_per_dozen = 2.25 / original
new_flour = flour_per_dozen * dozens

print("Your new recipe calls for:",new_flour,"cups of flour.")
print()


# baking soda

print("The original recipe calls for 1 teaspoon of baking soda.")
print()

bakingsoda_per_dozen = 1 / original
new_bakingsoda = bakingsoda_per_dozen * dozens

print("Your new recipe calls for:",new_bakingsoda,"teaspoons of baking soda.")
print()


# salt

print("The original recipe calls for 1 teaspoon of salt.")
print()

salt_per_dozen = 1 / original
new_salt = salt_per_dozen * dozens

print("Your new recipe calls for:",new_salt,"teaspoons of salt.")
print()


# butter

print("The original recipe calls for 2 sticks of butter.")
print()

butter_per_dozen = 2 / original
new_butter = butter_per_dozen * dozens

print("Your new recipe calls for:",new_butter,"sticks of butter.")
print()


# granulated sugar

print("The original recipe calls for 0.75 cup of granulated sugar.")
print()

gransugar_per_dozen = 0.75 / original
new_gransugar = gransugar_per_dozen * dozens

print("Your new recipe calls for:",new_gransugar,"cups of granulated sugar.")
print()


# brown sugar

print("The original recipe calls for 0.75 cup of brown sugar.")
print()

brownsugar_per_dozen = 0.75 / original
new_brownsugar = brownsugar_per_dozen * dozens

print("Your new recipe calls for:",new_brownsugar,"cups of brown sugar.")
print()


# vanilla extract

print("The original recipe calls for 1 teaspoon of vanilla extract.")
print()

vanilla_per_dozen = 1 / original
new_vanilla = vanilla_per_dozen * dozens

print("Your new recipe calls for:",new_vanilla,"teaspoons of vanilla extract.")
print()


# eggs

print("The original recipe calls for 2 large eggs.")
print()

eggs_per_dozen = 2 / original
new_eggs = eggs_per_dozen * dozens

print("Your new recipe calls for:",round(new_eggs),"large eggs.")
print()


# chocolate chips

print("The original recipe calls for 2 cups of chocolate chips.")
print()

chocchips_per_dozen = 2 / original
new_chocchips = chocchips_per_dozen * dozens

print("Your new recipe calls for:",new_chocchips,"cups of chocolate chips.")
print()









