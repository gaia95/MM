
dict1 = {"Key1" : "3H"}

dict2 = {"Key1" : "3H"}

dict3 = {"Key1" : "Hej"}

assert dict1 == dict2


if dict1 == dict2:  
    print("ja")

if not dict1 == dict3:
    raise AssertionError
    
assert dict1 == dict3