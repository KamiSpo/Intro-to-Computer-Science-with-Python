animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

animals['e'] = ['donkey']
animals['e'].append('dog')
animals['e'].append('dingo')

new_dict = {}
print(new_dict)

for k in animals:
    el = animals[k]
    if len(el) not in new_dict:
        new_dict[len(el)] = []
    new_dict[len(el)].append(k)
print(new_dict)
    
biggest = max(new_dict.keys())

print(new_dict[biggest])
print(new_dict.get(biggest))



