from functools import reduce
def reducible():
    product=reduce((lambda x,y:x*y),[1,2,3,4,5])
    print (">>>",product)
print(reducible)

