""""
Understanding Shallow Copy, Deep Copy, and Why Assignment (=) Doesn't Work for Copying in Python
"""
import copy

# 1. = Assignment
orginal = [1,2,3,[4,5],6]
copy_list = orginal
#check output
print("copy_list", copy_list) #output [1, 2, 3, [4, 5], 6]
print("orginal", orginal)
copy_list.append(7)
copy_list[len(copy_list)-2] = 12000

copy_list.insert(0, 900)
#check output
print("copy_list", copy_list) #[900, 2, 3, [4, 5], 6, 7]
print("orginal", orginal)
copy_list[4][1] = 100
#check output
print("copy_list", copy_list)
print("orginal", orginal)

dict_orginal = {"name": "John"}
dict_copy = dict_orginal
dict_copy["age"] =  300
print("copy_list", dict_orginal)
print("orginal", dict_copy)

#2. Shallow copy

orginal_shallow = [1,2,3,[4,5],6]
copy_list_shallow = copy.copy(orginal_shallow)

print("orginal_shallowlist", orginal_shallow)
print("copy_list_shallow", copy_list_shallow)

copy_list_shallow.insert(0, 800)
print("orginal_shallowlist", orginal_shallow) ##orginal_shallowlist [1, 2, 3, [4, 5], 6]
print("copy_list_shallow", copy_list_shallow) ##  copy_list_shallow [800, 1, 2, 3, [4, 5], 6]

copy_list_shallow.append(900)
print("orginal_shallowlist", orginal_shallow) ##orginal_shallowlist [1, 2, 3, [4, 5], 6]
print("copy_list_shallow", copy_list_shallow) ## copy_list_shallow [800, 1, 2, 3, [4, 5], 6, 900]

copy_list_shallow[1] = 12000
copy_list_shallow[4][1] = 55555555555*2
print("orginal_shallowlist", orginal_shallow) ##orginal_shallowlist [1, 2, 3, [4, 5], 6]
print("copy_list_shallow", copy_list_shallow) ## copy_list_shallow [800, 12000, 2, 3, [4, 5], 6, 900]


dict_orginal = {"name": "John" , "zip":{"code":5444}}
dict_copy = copy.copy(dict_orginal)
dict_copy["age"] =  300

if "address" not in dict_copy:
    dict_copy["address"] = {}
dict_copy["address"]['city'] =  "Western"

if dict_orginal.get('country',{}) is None:
    dict_orginal['country'] = {}
dict_orginal['country'] = "US"
dict_orginal['zip']['code'] = 8888888
dict_orginal['name'] = "Anne"

print("dict_orginal", dict_orginal) # {'name': 'Anne', 'zip': {'code': 8888888}, 'country': 'US'}
print("dict_copy", dict_copy) #{'name': 'John', 'zip': {'code': 8888888}, 'age': 300, 'address': {'city': 'Western'}}


