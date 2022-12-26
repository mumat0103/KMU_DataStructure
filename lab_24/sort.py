def seletion_sort(a):
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[min], a[i] = a[i], a[min]
            
a = [8, 4, 6, 9, 2, 3, 1]
seletion_sort(a)
print("seletion",a)

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j -1], a[j]
                
a = [8, 4, 6, 9, 2, 3, 1]
bubble_sort(a)
print("bubble", a)

def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        while j > 0 and a[j-1] > a[j]:
            a[j - 1], a[j] = a[j], a[j-1]
            j -= 1
        
a = [8, 4, 6, 9, 2, 3, 1]
insertion_sort(a)
print("insertion", a)

def shell_sort(a):
    n = len(a)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            key = a[i]
            j = i - interval
            while j >= 0 and a[j] > key:
                a[j + interval] = a[j]
                j -= interval
            a[j + interval] = key
        interval //= 2

a = [8, 4, 6, 9, 2, 3, 1]
shell_sort(a)
print("shell", a)

def quick_sort(a):
    def sort(low, high):
        if high <= low:
            return
        
        mid = partition(low, high)
        sort(low, mid -1)
        sort(mid, high)
    
    def partition(low, high):
        pivot = a[(low + high) // 2]
        while low <= high:
            while a[low] < pivot:
                low += 1
            while a[high] > pivot:
                high -= 1
            if low <= high:
                a[low], a[high] = a[high], a[low]
                low += 1
                high -= 1
        
        return low
    
    return sort(0, len(a) - 1)
    

a = [8, 4, 6, 9, 2, 3, 1]
quick_sort(a)
print("quick", a)

def merge_sort(a):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)
        
    def merge(low, mid, high):
        tmp = []
        l, h = low, mid
        
        while l < mid and h < high:
            if a[l] < a[h]:
                tmp.append(a[l])
                l += 1
            else:
                tmp.append(a[h])
                h += 1
                
        while l < mid:
            tmp.append(a[l])
            l += 1
        while h < high:
            tmp.append(a[h])
            h += 1
            
        for i in range(low, high):
            a[i] = tmp[i - low]
            
    return sort(0, len(a))

a = [8, 4, 6, 9, 2, 3, 1]
merge_sort(a)
print("merge", a)

def heapify(a, idx, len):
    c = idx * 2
    p = a[idx]

    while c < len:
        if a[c] < a[c+1]:
            c += 1
            
        if p > a[c]:
            break
            
        a[c//2], a[c] = a[c], a[c//2]
        c *= 2

    a[c//2] = p

def heap_sort(a):
    n = len(a)
    for i in range(n - 1, 0, -1):
        a[1], a[i] = a[i], a[1]
        heapify(a, 1, i - 1)
    
a = [8, 4, 6, 9, 2, 3, 1]
a = [None] + a
n = len(a)
for i in range(n//2, 0, -1):
    heapify(a, i, n)
heap_sort(a)
print("heap", a)