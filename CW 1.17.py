#states and their abbrevations
'''
states = {
  'Oregon' : 'OR',
  'Florida' : 'FL',
  'California' : 'CA',
  'New York' : 'NY',
  'Michigan' : 'MI'
}

#cites of states
cities = {
  'CA' : 'San Francisco',
  'MI' : 'Detroit',
  'FL' : 'Jacaksonville'
}

#adding more cities to the dictionary
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#printing cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#printing abbeviations for states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#printing every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in a state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#printing both abbreviation and cities for state
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
state = states.get('Texas')
if not state:
    print("Sorry, no Texas")
city = cities.get("TX", 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

#1. create a dictionary
#2. add 3 key-values to it
#3. write a loop to iterate over the dictionary and print out each key-value pair
#4. check if a given value is in the dictionary or not

#prices of cryptocurrencies today
cryptoprice = {
  'BTC' : '$11,000',
  'ETH' : '$1000',
  'LTC' : '$200'
}

#cryptocurrencies and their abbreviation
coins = {
  'Bitcoin' : "BTC",
  'Ethereum' : "ETH",
  'Litecoin' : 'LTC'
}



for coins, abbrev in list(coins.items()):
  print(f" {coins} : {abbrev}")
for cryptoprice, price in list(cryptoprice.items()):
  print(f" {cryptoprice} : {price}")



#using a dictionary to count the number of times a character appears in a string
d = {} #OR d = dict()
#get char using index OR get just the character

s = input('Enter a string: ')
s = list(s)

#for i in range(0,len(s)):
#  c = s[i]

for c in s:
  if c in d:
    d[c] += 1
  else:
    d[c] = 1
for x in d:
  print(f'{x} : {d[x]}')

#for x, y in list(d.items()):
#  print(f'{x} : {y}')
'''
