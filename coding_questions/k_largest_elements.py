import heapq

def k_largest(v,N,K):
    largest_elements=heapq.nlargest(K,v)
    print("Size of array:" , N)
    return largest_elements

arr=list(map(int,input("Enter the elements:").split()))
k=int(input("Enter the kth value:"))
N=len(arr)

k_largest_elements=k_largest(arr,N,k)
print("kth_largest_element: " , k_largest_elements[-1])