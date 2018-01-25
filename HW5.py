#HW5

'''
#1. python program to iterate over dictionaries using for loops
a = {1 : 'January', 2 : 'February', 3 : 'March', 4 : 'April', 5 : 'May', 6 : 'June', 7 : 'July', 8 : 'August', 9 : 'September', 10 : 'October', 11 : 'November', 12 : 'December'}
for month_key, value in a.items():
     print(month_key, ':', a[month_key])
'''

#2. python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
#example for: d = {n = 5}
#output: {1:1, 2:4, 3:9, 4:16, 5:15}

n = int(input("Please enter the numbers that you want to square: "))
di = {}
counter = 0
while counter < n:
  counter += 1
  di[counter] = counter ** 2
print(di)


'''
#DISREGARD
#3. python program to remove duplicates from dictionary (entry with the same key and value)
c = {1:2, 3:4, 5:5, 6:6}
for kee, valu in c.items():
    if kee == valu:
      del c[kee]

'''

#4. function that takes a string as a parameter and returns a dictionary. keys should be the chracters in the string and values are the number of times each character appears; excluding punctuation and spaces.

'''
d = {} #OR d = dict()
#get char using index OR get just the character

s = input('Enter a string: ')
s = list(s)

#list of special characters
spchar = [" ", ",", ".", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "<", ">", "?", "/", "`", "~", "[", "]", "{", "}", "|", ":", ";"]

#for i in range(0,len(s)):
#  c = s[i]

for c in s:
  if c in d:
    d[c] += 1
  elif c in spchar:
    pass
  elif c == '"':
    pass
  elif c == "'":
    pass
  else:
    d[c] = 1
for x in d:
  print(f'{x} : {d[x]}')

#for x, y in list(d.items()):
#  print(f'{x} : {y}')
'''
