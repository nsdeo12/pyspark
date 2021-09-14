def findKthLargest(k,testArr):
    testArr.sort(reverse=True)
    print(testArr)
    return testArr[k-1]
if __name__=='__main__':
    tA=[12, 3, 5, 7, 19]
    k=int(input('enter kth value'))
    print(k ,'nd largest element is : ',findKthLargest(k,tA))
