s = 'abcabcdabcde'

current_string = s[0]
longest_string = current_string

for i in range(1, len(s)):
    print('current state of my program is: string={} i={}'.format(current_string, i))
    
    if ord(s[i-1]) < ord(s[i]):
        current_string += s[i]
    else:
        if len(current_string) > len(longest_string):
            longest_string = current_string
        current_string = s[i]

if len(current_string) > len(longest_string):
    longest_string = current_string

print(longest_string)


string = ""
longest_string = ""

for i in range(len(s)-1):
    print('current state of my program is: string={} i={}'.format(string, i))
    if ord(s[i]) < ord(s[i + 1]):
        string += s[i]
    else:
        string += s[i]
        if len(string) > len(longest_string):
            longest_string = string
            string = ""
        else:
            string = ""

string += s[i+1]
if len(string) > len(longest_string):
    longest_string = string

print(longest_string)