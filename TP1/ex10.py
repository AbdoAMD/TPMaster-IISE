#from typing import Counter
from typing import Counter


def fusionner_dicts(dict1, dict2):
    return dict(Counter(dict1) + Counter(dict2))


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

resultat = fusionner_dicts(dict1, dict2)
print(resultat)