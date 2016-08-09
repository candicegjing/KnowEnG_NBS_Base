

import yaml
import os


from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))

test_file = dir_path + '/' + 'test_sorted.yml'
compare_file = dir_path + '/' + 'compare_sorted.yml'
test_dict = None
comp_dict = None
with open(test_file, 'r') as stream:
    try:
        test_dict = yaml.load(stream)
        print(type(test_dict))
    except yaml.YAMLError as exc:
        print(exc)
stream.close()


with open(compare_file, 'r') as stream:
    try:
        comp_dict = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)
stream.close()


v = defaultdict(list)
for key, value in sorted(test_dict.items()):
    v[value].append(key)

print (v)







