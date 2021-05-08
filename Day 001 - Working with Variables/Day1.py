print("\"Hello World\"")

print("Hello World \nHello World \nHello World")

print("Hello" + " Brent")

print ("Hello " + input("Enter your Name:")+"!")

personName = input("Enter your Name:")
print(personName)

lastName = "Littlefield"
print(personName+" " + lastName)

name = input("Your Name is?")
length = len(name)
print(length)


a = input("a: ")
b = input("b: ")

temp = a
a = b
b = temp

print("a: " + a)
print("b: " + b)

## DAILY PROJECT FOR DAY 001

#1. Create a greeting for your program.
print("Hello! Welcome to Band Name Generator!")

#2. Ask the user for the city that they grew up in.
city = input("Please Enter the Name of the City in Which you grew up \n ")

#3. Ask the user for the name of a pet.
petName = input("Please Enter the Name of your Favourite Pet \n ")

#4. Combine the name of their city and pet and show them their band name.
bandName = city+" "+petName
print(bandName)
# OR 
#print(city+" "+petName)
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/