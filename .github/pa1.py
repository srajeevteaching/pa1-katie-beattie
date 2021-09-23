# Team Members: Katie Beattie
# Course: CS151, Dr. Rajeev
# September 22, 2021
# Programming Assignment 1
# Program inputs include length, width, and height.
# Program outputs include the total area of the room to be painted.

lengthInput = input("Enter the length of your room (in feet) here. ")
lengthInt = int(lengthInput)
widthInput = input("Enter the width of your room (in feet) here. ")
widthInt = int(widthInput)
heightInput = input("Enter the height of your room (in feet) here. ")
heightInt = int(heightInput)

area = ((2 * (lengthInt * heightInt)) + (2 * (widthInt * heightInt)) + (lengthInt * widthInt))
primer = area / 200
paint = area / 350
print("The area of your room is ", area, " square feet.")
print("You will need ", primer, " gallons of primer to paint the walls in your room.")
print("You will need ", paint, "gallons of paint.")
