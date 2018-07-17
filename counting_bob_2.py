s = 'dfdpfbobewerbobfefduubobiugygbobrbob'
i= 0
bob_counter = 0
for i in range((len(s)-2)):
    char1 = s[i]
    char2 = s[(i + 1)]
    char3 = s[(i + 2)]
    print(char1 + char2 + char3)
    if char1 + char2 + char3 == str('bob'):
         bob_counter += 1
         print(bob_counter)

    
print('Number of times bob occurs is: ' + str(bob_counter))