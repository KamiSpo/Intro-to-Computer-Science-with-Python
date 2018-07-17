#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2

s = 'azcbobobeggdsfsiebobhakhaehrerbobbobklbo'
bob_number = 0
end = len(s) - 1
index = 0

for letter in s:
    if index + 2 >= len(s):
        break
    
    if letter is 'b':
        second = s[index + 1]
        if second is 'o':
            last = s[index + 2]
            if last is 'b':
                bob_number += 1
    index += 1
print('Number of times bob occurs is; ' + str(bob_number))



