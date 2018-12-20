'''
Quicksort
Pivot is always the last element of the list
'''

def quick_sort(A, low, high):
    print("\n-----------Low = {}, High = {}".format(low, high))
    # If more than 1 Item in list to be sorted
    if(low < high):
        p = partition(A, low, high)
        # All items left of pivot
        quick_sort(A, low, p - 1)
        # All items right of pivot
        quick_sort(A, p + 1, high)

def partition(A, low, high):
    # Set pivot
    pivot = A[high]
    print("Pivot = {} (A[{}])".format(pivot, high))
    border = low - 1
    print("Border = {}".format(border))
    # Loop from first element of list to the (last-1)th element (last is not included bcuz pivot)
    for index in range(low, high): # range will be from 0 to high-1
            # Compare current element of list with pivot element
            if(A[index] <= pivot):
                border += 1
                # swap A[border] with A[index]
                print("Swapping A[{}] ({}) with A[{}] ({}) because {} (A[{}]) <= {}".format(border, A[border], index, A[index], A[index], index, pivot))
                print("Before swap:\n{}".format(A))
                A[border], A[index] = A[index], A[border]
                print("After swap:\n{}\n--------------------------\n".format(A))
    # Swap A[border + 1] with A[high] (put the pivot element (last elem) to the position with index (border + 1))
    print("\nSwapping PIVOT element ({}) with element with index ({})".format(A[high], (border+1)))
    print("Before swap:\n{}".format(A))
    A[border + 1], A[high] = A[high], A[border + 1]
    print("After swap:\n{}\n--------------------------\n".format(A))
    return (border + 1)

global A
A = [24149, 13647, 29614, 47539, 30326, 13529, 88222, 81550, 31122]
print("Initial array:")
print(A)
low = 0
high = (len(A) -1)

quick_sort(A, low, high)
print(A)
