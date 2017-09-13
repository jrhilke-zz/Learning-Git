def MergeSort(A):
    if len(A)==1:
        return A
    n = len(A)

    first_half=A[:n/2]
    second_half=A[n/2:]
    return MergeSort(A[:n/2])+MergeSort(A[n/2:])
A = [1,5,3,6,7,2,10]
