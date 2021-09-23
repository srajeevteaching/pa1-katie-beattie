# Team Members: Katie
# Course: CS151, Dr. Rajeev
# September 22, 2021
# Programming Assignment 1
# Program inputs include length, width, and height.
# Program outputs include the total area of the room to be painted.

# Prompt for length, width, and height of room.
lengthInput = input("Enter the length of your room (in feet) here. ")
# Typecast to int
lengthInt = int(lengthInput)
# Above steps repeated
widthInput = input("Enter the width of your room (in feet) here. ")
widthInt = int(widthInput)
heightInput = input("Enter the height of your room (in feet) here. ")
heightInt = int(heightInput)

# Calculated area of the room (not including floor
area = ((2 * (lengthInt * heightInt)) + (2 * (widthInt * heightInt)) + (lengthInt * widthInt))
# Sq. ft divided by values for paint and primer
primer = (area // 200) + 1
paint = (area // 350) + 1
# Outputs area, gallons of primer and paint
print("The area of your room is ", area, " square feet.")
print("You will need ", primer, " gallons of primer to paint the walls in your room.")
print("You will need ", paint, " gallons of paint.")
