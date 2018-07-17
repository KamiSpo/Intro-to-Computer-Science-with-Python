s = 'kamilaspodymek'
vowels = 0
for letter in s:
    if letter in str('aeiou'):
        vowels += 1
print('Number of vowels: ' + str(vowels))