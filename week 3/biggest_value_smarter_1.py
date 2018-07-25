animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

animals['e'] = ['donkey']
animals['e'].append('dog')
animals['e'].append('dingo')

current_max = 0
current_max_list = []

for k in animals:
    el = animals[k]

    if len(el) > current_max:
        current_max_list = [k]
        current_max = len(el)
    elif len(el) == current_max:
        current_max_list.append(k)
    
print(current_max_list)