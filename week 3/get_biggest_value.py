animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

new_dict = {}
print(new_dict)

for k in animals:
    el = animals[k]
    new_dict[len(el)] = []
print(new_dict)

for k in animals:
    el = animals[k]
    new_dict[len(el)].append(k)

biggest = max(new_dict.keys())

print(new_dict[biggest])
print(new_dict.get(biggest))
