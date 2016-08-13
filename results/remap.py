

import yaml
import os


from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))

test_file = dir_path + '/' + 'test_sorted.yml'
compare_file = dir_path + '/' + 'golden_sorted.yml'
test_dict = None
comp_dict = None
with open(test_file, 'r') as stream:
    try:
        test_dict = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)
stream.close()


with open(compare_file, 'r') as stream:
    try:
        comp_dict = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)
stream.close()


v_test = defaultdict(list)
for key, value in sorted(test_dict.items()):
    v_test[value].append(key)
#print(v_test)


v_golden = defaultdict(list)
for key, value in sorted(comp_dict.items()):
    v_golden[value].append(key)
#print(v_golden)

for key, value in v_golden.items():
    cur_len = len(value)
    diff = 9999
    for k, v in v_test.items():
        diff_set = list(set(value) - set(v))
        #if len(diff_set) < diff:
        #    diff = len(diff_set)
        print("{} <---> {} with difference {}".format(key, k, len(diff_set)))




map1_0 = list(set(v_golden[1]) - set(v_test[0]))
print("golden 0  <--> test 1 diff on {} over {}".format(map1_0, len(v_golden[1])))
map2_2 = list(set(v_golden[2]) - set(v_test[2]))
print("golden 2  <--> test 2 diff on {} over {}".format(map2_2, len(v_golden[2])))

map1_3 = list(set(v_golden[3]) - set(v_test[1]))
print("golden 3  <--> test 1 diff on {} over {} ".format(map1_3, len(v_golden[3])))







