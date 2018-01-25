#HW2
'''
What do the following commands do in linux?
a. CD - change directory to navigate the file system
b. LS - same as dir; it lists all files withina folder/directory
c. TOUCH - creates and empty file or accesses a file without opening/reading it. The only thing affected is the timestamp.

#letter grade for score
#90 - 100 = A
#80 - 89 = B
#70 - 79 = C
#less than 70 = "Not acceptable. Pay attention"

#determine if input number is even or odd

#user selections option and function converts accordingly
#options are as follows:
#KB to bytes
#MB to bytes
#TB to bytes
'''
def grade()
  x = input("What is your numberical score?")
  if x => 90 and x <= 100
  print("You got an A!")
  elif x => 80 and x <= 90
  print("You got a B")
  elif x => 70 and x <= 79
  print("You got a C")
  elif x <= 70
  print("That is not acceptable. Please pay attention next time")
  elif x > 100
  print("I didn't assign bonus points so you must have cheated!")
  elif x < 0
  print("I wouldn't give you a negative score. Please run the function again")
grade()

def oddseven()
  y = input("Give me a number and I will tell you if it is odd or even")
  if y % 2 = 0
  print("Your number is even")
  elif y % 2 = 1
  print("Your number is odd")
oddseven()

def convertbytes()
  print("I can convert your kilobytes, megabytes and terabytes into bytes using binary")
  print("Conversions in decimal are simple enough. There are 1000 or 1*10^3 bytes in a kilobyte, 1,000,000 or 1*10^6 bytes in a megabyte and 1*10^12 bytes in a terabyte")
  print("\n Please follow the prompt and enter 1 to convert KB, 2 to convert MB, or 3 to convert TB")
  z = input("Please enter the number of units you want to convert: ")
  byte = input("Please choose option 1, 2, or 3 now: ")
  if byte = 1
    print(f"There are {z * 2 ** 10} byes in {z} kilobytes.)
  elif byte = 2
    print(f"There are {z * 2 ** 20} bytes in {z} megabytes.)
  elif byte = 3
    print(f"There are {z * 2 ** 40} bytes in {z} terabytes.)

convertbytes()

  #1024 (2^10)
  #1,048,576 (2^20)
  #1,099,511,627,776 (2^40)
