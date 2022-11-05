from itertools import product
 
def cartesian_product(arr1, arr2):
 
    # return the list of all the computed tuple
    # using the product() method
    return list(product(arr1, arr2))
   
# Driver Function
if __name__ == "__main__":
    arr1 = ['ab', 'ba']
    arr2 = ['c']
    arr3=['def', 'edf', 'dfe']
    m_1=(cartesian_product(arr1, arr2))
    print("".join(m_1))
    print(m_1)
    n=(cartesian_product(m_1, arr3))
    print(n)
    for i in n:
        m=''.join(str(i))
        print(m)
   
    #print(n)
