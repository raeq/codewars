'''
https://discord.com/channels/267624335836053506/696354453724594176/827878807783604235
'''

l1 = ['apple', 'bear', 'sun', 'france', 'italy']
weights = {'sun': 1,
           'france': 20,
           'bear': 30,
           'apple': 40}

print(sorted(l1, key = lambda x: weights.get(x, 100)))
