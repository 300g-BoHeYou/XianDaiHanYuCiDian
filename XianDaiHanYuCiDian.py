from json import load
from re import split

def my_obj_pairs_hook(lst):
    result={}
    count={}
    for key,val in lst:
        if key in count:
            count[key]=1+count[key]
        else:
            count[key]=1
        if key in result:
            if count[key] > 2:
                result[key].append(val)
            else:
                result[key]=[result[key], val]
        else:
            result[key]=val
    return result

with open("XDHYCD7th.json",'r',encoding='utf-8') as f:
    dictionary = load(f,strict=False, object_pairs_hook=my_obj_pairs_hook)

while True:
    key = input("\n要查的词：")
    if key == 'Q':
        break
    elif key in dictionary.keys():
        mean = dictionary[key]
        print(key,"的解释是：")
        if type(mean) == list:
            for i in mean:
                [print(j) for j in split("❶|❷|❸|❹|❺|❻|❼|❽|❾|❿",i)]
                print("\n")
        else:
            [print(j) for j in split("❶|❷|❸|❹|❺|❻|❼|❽|❾|❿",mean)]
            print("\n")
        
    else:
        print("查无该词")