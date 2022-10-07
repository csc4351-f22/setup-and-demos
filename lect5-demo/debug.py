import math

def my_function(some_int):
    for i in range(some_int):
     print(i)

    print("done")

my_function(5)


def my_other_function(arr1, arr2):
    import pdb
    pdb.set_trace()
    d = {}
    for i in range(len(arr1)):
        d[arr1[i]] = arr2[i+1]
    
    for num in arr2:
        print(d[num])

my_other_function([1,2,3],[2,3,4])



