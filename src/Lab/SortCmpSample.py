from functools import cmp_to_key
from random import randrange

data = [
    {'fst': randrange(0, 101, 2), 'snd': randrange(0, 101, 2)} for i in range(20)
]

print(data)
data.sort(key = cmp_to_key(lambda x, y: 1 if ((x['fst'] < y['fst']) and (x['snd'])>y['snd']) else (0 if ((x['fst'] == y['fst']) and (x['snd']) == y['snd']) else -1 ) ))
print(data)