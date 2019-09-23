# MPG CALCULATOR MBAY0003
#!/usr/bin/env python
milesDriven = float(input("ENTER NUMBER OF MILES DRIVEN : "))
gallonsUsed = float(input("ENTER AMOUNT OF GAS USED [GALONS] : "))
milesPerGallon = milesDriven / gallonsUsed
print("The car's MPG is:" + str(milesPerGallon))