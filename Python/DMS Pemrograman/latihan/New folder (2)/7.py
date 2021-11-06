def tukar(A):
    #lengkapi fungsi berikut
    a = A[0]
    A[0] = A[-1]
    A[-1] = a
    return A

list_bilangan = list(map(int, input().split()))