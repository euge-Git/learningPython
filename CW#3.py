####### REVIEW- WEDNESDAY 01/03 ############
####### NAME:

##NOTE Following questions are the same from the slide.
###Complete the following questions and submit by the end of class
### you MUST add comments to explain your Solution or approach to the problem

##1.Write a Python function to find those numbers which are divisible by 7 between 1500 and 2700 (both included).
##TODO: Solution

def div7():
#range from 1500 - 2700
  for x in range(1500,2701):
#if x modulus 7 equals to 0, then print x
    if (x % 7) == 0:
      print(x)
#run function
div7()

##2.Write a Python program to convert temperatures to and from celsius and fahrenheit.
'''[Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius '''
##TODO: Solution

def conversion():
  choose = input("Enter CTF to convert Celsius to Farenheit or FTC to convert Farenheit to Celsius")
  deg = int(input("What is the unit that you want to convert?"))
  if choose.upper() == 'CTF':
    x = 32 + ((deg*9)/5)
    print(x)
  elif choose.upper() == 'FTC':
    y = ((deg-32)*5)/9
    print(y)

conversion()

##3.Write a Python program that accepts a word from the user and reverse it.
##TODO: Solution
#for i in range(0, len(s)):
#    print(i, s[i])

def reverse_string():
    s = input("Enter a string: ")
    for i in range(len(s)-1, -1, -1):
      #range(0,10) <--> range(10,0,-1)
#s[-1] is the same as s.len()-1
      print(i, s[i])
      r = r+s[i] #string concatenate
     print(r)

reverse_string()

##4. Write a Python program that accepts a string and calculate the number of digits and letters.
'''Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2'''
##TODO: Solution

##5. Write a Python program to check whether an alphabet is a vowel or consonant.
'''Expected Output:

Input a letter of the alphabet: k
k is a consonant.'''
##TODO: Solution

def is_vowel():
    x = input("Enter a string: ")
    s = x.lower()
    if ('a' in s) or ('e' in s) or ('i' in s) ('o' in s) or ('u' in s):
        print("String has a vowel")
    else:
        print(False)

def vowcon():
  x = input("Enter a letter of the alphabet and I will tell you if it is a vowel or consonant: ")
  if x == 'a':
    print("This is a vowel")
  elif x == 'A':
    print("This is a vowel")
  elif x == 'e':
    print("This is a vowel")
  elif x == 'E':
    print("This is a vowel")
  elif x == 'I':
    print("This is a vowel")
  elif x == 'i':
    print("This is a vowel")
  elif x == 'o':
    print("This is a vowel")
  elif x == 'O':
    print("This is a vowel")
  elif x == 'u':
    print("This is a vowel")
  elif x == 'U':
    print("This is a vowel")
  elif type(x) == int:
    print("This is a number, not a letter")
  else:
    print("This is a consonant")

vowcon()


##6. Write a Python program to convert month name toa number of days.
'''Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December
Input the name of Month: February
No. of days: 28/29 days '''
##TODO: Solution
def monthdays():
  month = input("Please enter a month and I will tell you how many days there are in it: ")
  if month.lower() == 'january' or month.lower() == 'march' or month.lower() == 'may' or month.lower() == 'july':
    print("There are thirty one days in this month")
  elif month.lower() == 'april' or month.lower() == 'june' or month.lower() == 'september' or month.lower() == 'november':
    print("There are thirty days in this month")
  elif month.lower() == 'february':
    print("There are twenty eight days in this month, but on a leap year there are twenty nine days")
  else:
    print("What you gave me is not a month. Please check your spelling")

monthdays()
##7. Write a Python program to display astrological sign for given date of birth.
'''Expected Output:

Input birthday: 15
Input month of birth (e.g. march, july etc): may
Your Astrological sign is : Taurus '''
##TODO: Solution

##8. Write a Python program to find the median of three values.
'''Expected Output:

Input first number: 15
Input second number: 26
Input third number: 29
The median is 26.0'''


print("I can give you the median of three numbers")

def median():
  first = input("What is the first number? ")
  second = input("What is the second number? ")
  third = input("What is the third number? ")
  if first > second and first < third:
    print(first)
  elif first < second and first > third:
    print(first)
  elif second > first and second < third:
    print(second)
  elif second < first and second > third:
    print(second)
  elif third > first and third < second:
    print(third)
  elif third < first and third > second:
    print(third)

median()

##9. write a for loop that iterates over a string entered by user and counts how many times letter ‘a’ appeared in that string
##TODO: Solution


##10. Write a function that counts down to zero from one of the following, 10, 15, 20. User will pick one of the options
