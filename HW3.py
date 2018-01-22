#EXERCISE 21
'''
#defining an addition function with arguments a and b; returns value
def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b
#defining a subtraction function with arguments a and b; returns value
def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
#defining a multiplcation function with arguments a and b; returns value
def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b
#defining a division function with agruments a and b; returns value
def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

#printing statement before functions are run
print("Let's do something with just functions!")

#age variable is assigned to the value 35 through the add(30,5) function
age = add(30, 5)
#height variable is assigned the value of 70 through the subtract(74,4) function
height = subtract(74, 4)
#weight variable is assigned the value of 180 through the multiply(90,2) function
weight = multiply(90, 2)
#iq variable is assigne dhte value of 50 through the divide(100,2) function
iq = divide(100, 2)

#prints statments and values of the variables that have just been assined
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


#A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

#what variable is assigned by using functions as arguments
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

#EXERCISE 25
#function to break up words
def break_words(stuff):
    words = stuff.split(' ')
    return words
#function to sort words
def sort_words(words):
    return sorted(words)
#function to print the first word
def print_first_word(words):
    word = words.pop(0)
    print(word)
#function to print the last word
def print_last_word(words):
    word = words.pop(-1)
    print(word)
#function takes a sentence, calls the break_words function to split, calls/returns sort_words function
def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)
#function to print first/last words in a sentence by using break_words, and calling the print (first/last) word function
def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
#function to sort and then print the first and last word in a sentence. calls the sort_sentence function and prints first/last word
def print_first_and_last_sorted(sentence):
    words = sort_stentence(sentence)
    print_first_word
    print_last_word

#imported exercise 25 in a serparte file.py and imported it from terminal.
#shortcut for importing can be done as follows:
#from [filename] import * [everything/wildcard]
#defined the variable "sentence" and proceeded to break up the words, sort the words, and print the first/last words of the different groups



#EXERCISE 29
people = 20
cats = 30
dogs = 15

#if statements for comparing the number of people to cats and dogs with respective print statements
if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drolled on!")

if people > dogs:
    print("The world is dry!")

#dogs variable has 5 units added to it and is reassigned that value
dogs += 5

#if statements comparing the new value of dogs to people with respective print statements
if people >= dogs:
    print("People are greather than or equal to dogs.")
if people <= dogs:
    print("People are less than or equal to dogs.")
if people == dogs:
    print("People are dogs.")


#EXERCISE 30
#assigning values to variables
people = 30
cars = 40
trucks = 15

#if statements comparing the number of cars to people
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

#if statements comparing the number of trucks to cars
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

#if statement comparing people to trucks
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

#EXERCISE 31
#opening statement to story
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

#takes user input to choose a door
door = input("> ")

#first option depicts a bear with further prompts
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream a the bear.")

#takes user input to decide what to do with the bear
    bear = input("> ")
#results for choosing what to do with the bear
    if bear = "1"
        print("The bear eats your face off. Good job!")
    elif bear == "2"
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.)
        print("Bear runs away.")

#second option tranports you into a Lovecraftian pocket universe
elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
#takes user input to try and comprehend the behemoth elder god
    insanity = input("> ")
#mere humans are driven to insanity upon gazing upon Cthulhu
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of a jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")

#not choosing a door will also kill you
else:
    print("You stumble around and fall on a knife and die. Good job!")


1. From​ ​the​ ​book​ ​Learn​ ​Python​ ​the​ ​Hard​ ​Way,​ ​complete​ ​exercise​ ​21,​ ​25,​ ​29,​ ​30​ ​and​ ​31.
2. Write​ ​a​ ​function​ ​that​ ​converts​ ​minutes​ ​to​ ​seconds​ ​and​ ​should​ ​work​ ​for​ ​any​ ​number​ ​of
minutes​ ​entered​ ​by​ ​user.​ ​Test​ ​your​ ​function​ ​with​ ​the​ ​following:​ ​How​ ​many​ ​seconds​ ​are
there​ ​in​ ​42​ ​minutes​ ​42​ ​seconds?
3. write​ ​a​ ​loop​ ​that​ ​traverse​ ​through​ ​a​ ​string​ ​provided​ ​by​ ​the​ ​user​ ​and​ ​prints​ ​out​ ​one​ ​letter
at​ ​a​ ​time.
4. Write​ ​a​ ​function​ ​that​ ​takes​ ​two​ ​parameters:​ ​a​ ​user​ ​input​ ​as​ ​string​ ​and​ ​a​ ​user​ ​input​ ​as​ ​a
character.​ ​The​ ​function​ ​searches​ ​for​ ​how​ ​many​ ​times​ ​the​ ​letter​ ​appears​ ​in​ ​the​ ​string.
5. write​ ​a​ ​boolean​ ​function​ ​(review​ ​boolean​ ​if​ ​you​ ​need​ ​to)​ ​that​ ​returns​ ​true​ ​or​ ​false​ ​if​ ​the
letter​ ​x​ ​is​ ​in​ ​a​ ​string​ ​provided​ ​by​ ​the​ ​user.
6. write​ ​a​ ​boolean​ ​function​ ​that​ ​returns​ ​true​ ​or​ ​false​ ​if​ ​any​ ​of​ ​the​ ​letter​ ​a,​ ​e,​ ​i,​ ​o,​ ​u​ ​and​ ​in​ ​a
string​ ​provided​ ​by​ ​the​ ​user.
7. What​ ​is​ ​the​ ​volume​ ​of​ ​a​ ​sphere​ ​with​ ​radius​ ​5?​ ​The​ ​volume​ ​of​ ​a​ ​sphere​ ​with​ ​radius​ ​r​ ​is
(4/3)πr3​ ​.
8. Write​ ​a​ ​boolean​ ​function​ ​that​ ​returns​ ​true​ ​if​ ​a​ ​given​ ​input​ ​is​ ​divisible​ ​by​ ​3​ ​or​ ​return​ ​false
otherwise.
9. find​ ​the​ ​length​ ​of​ ​the​ ​string​ ​given​ ​by​ ​the​ ​user​ ​as​ ​input​ ​using​ ​a​ ​counter​ ​variable​ ​(don’t​ ​use
the​ ​built-in​ ​len​ ​function)
'''

'''
1. From​ ​the​ ​book​ ​Learn​ ​Python​ ​the​ ​Hard​ ​Way,​ ​complete​ ​exercise​ ​21,​ ​25,​ ​29,​ ​30​ ​and​ ​31.
2. Write​ ​a​ ​function​ ​that​ ​converts​ ​minutes​ ​to​ ​seconds​ ​and​ ​should​ ​work​ ​for​ ​any​ ​number​ ​of
minutes​ ​entered​ ​by​ ​user.​ ​Test​ ​your​ ​function​ ​with​ ​the​ ​following:​ ​How​ ​many​ ​seconds​ ​are
there​ ​in​ ​42​ ​minutes​ ​42​ ​seconds?
3. write​ ​a​ ​loop​ ​that​ ​traverse​ ​through​ ​a​ ​string​ ​provided​ ​by​ ​the​ ​user​ ​and​ ​prints​ ​out​ ​one​ ​letter
at​ ​a​ ​time.
4. Write​ ​a​ ​function​ ​that​ ​takes​ ​two​ ​parameters:​ ​a​ ​user​ ​input​ ​as​ ​string​ ​and​ ​a​ ​user​ ​input​ ​as​ ​a
character.​ ​The​ ​function​ ​searches​ ​for​ ​how​ ​many​ ​times​ ​the​ ​letter​ ​appears​ ​in​ ​the​ ​string.
5. write​ ​a​ ​boolean​ ​function​ ​(review​ ​boolean​ ​if​ ​you​ ​need​ ​to)​ ​that​ ​returns​ ​true​ ​or​ ​false​ ​if​ ​the
letter​ ​x​ ​is​ ​in​ ​a​ ​string​ ​provided​ ​by​ ​the​ ​user.
6. write​ ​a​ ​boolean​ ​function​ ​that​ ​returns​ ​true​ ​or​ ​false​ ​if​ ​any​ ​of​ ​the​ ​letter​ ​a,​ ​e,​ ​i,​ ​o,​ ​u​ ​are​ ​in​ ​a
string​ ​provided​ ​by​ ​the​ ​user.
7. What​ ​is​ ​the​ ​volume​ ​of​ ​a​ ​sphere​ ​with​ ​radius​ ​5?​ ​The​ ​volume​ ​of​ ​a​ ​sphere​ ​with​ ​radius​ ​r​ ​is
(4/3)πr3​ ​.
8. Write​ ​a​ ​boolean​ ​function​ ​that​ ​returns​ ​true​ ​if​ ​a​ ​given​ ​input​ ​is​ ​divisible​ ​by​ ​3​ ​or​ ​return​ ​false
otherwise.
9. find​ ​the​ ​length​ ​of​ ​the​ ​string​ ​given​ ​by​ ​the​ ​user​ ​as​ ​input​ ​using​ ​a​ ​counter​ ​variable​ ​(don’t​ ​use
the​ ​built-in​ ​len​ ​function)
'''

'''
#2
def convertmin():
    m = int(input("How many minutes? "))
    s = int(input("How many seconds? "))
    m60 = (m * 60)
    total = (m60 + s)
    print(f"For {m} minutes and {s} seconds, there are {total} seconds.")
convertmin()

#3
datstring = input("What is your string of characters? ")
for x in datstring:
    print(x)

#4
def searchstring():
    strng = input("What is your string? ")
    char = input("What character are you searching for in the string? ")
    count = 0
    for x in strng:
        if x == char:
            count = count + 1
    print(f'The character {char} appears {count} times in the {strng}')

#5
striing = input('What is your string? I will check for the letter "X" in it. ')
if 'X' in striing:
    result = True
    return result
    print('It is true that the letter "X" is in your string')
elif 'x' in striing:
    result = True
    return result
    print('It is true that the letter "x" is in your string')
else:
    result = False
    return result
    print('The letter "X" is not in your string')

#6
strang = input('What is your string? I will check if there are vowels in it. ')
if 'A' in strang:
    result = True
    return result
    print('It is true that the letter "A" is in your string')
elif 'a' in strang:
    result = True
    return result
    print('It is true that the letter "a" is in your string')
elif 'E' in strang:
    result = True
    return result
    print('It is true that the letter "E" is in your string')
elif 'e' in strang:
    result = True
    return result
    print('It is true that the letter "e" is in your string')
elif 'I' in strang:
    result = True
    return result
    print('It is true that the letter "I" is in your string')
elif 'i' in strang:
    result = True
    return result
    print('It is true that the letter "i" is in your string')
elif 'O' in strang:
    result = True
    return result
    print('It is true that the letter "O" is in your string')
elif 'o' in strang:
    result = True
    return result
    print('It is true that the letter "o" is in your string')
elif 'U' in strang:
    result = True
    return result
    print('It is true that the letter "U" is in your string')
elif 'u' in strang:
    result = True
    return result
    print('It is true that the letter "u" is in your string')
else:
    result = False
    return result
    print('There are no vowels in your string')


#7
import math
def volsphere():
    rad = int(input("Please enter a value for the radius of your sphere (e.g. 5) "))
    volume = 4/3*math.pi*rad**3
    print(f'The volume of a sphere with a radius of {rad} is {volume} units')
volsphere()
#8

#9
'''
