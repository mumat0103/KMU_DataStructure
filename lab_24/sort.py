def seletion_sort(a):
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        
        if min != i:
            a[min], a[i] = a[i], a[min]
            
a = [8, 4, 6, 9, 2, 3, 1]
seletion_sort(a)
print(a)

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j -1], a[j]
                
a = [8, 4, 6, 9, 2, 3, 1]
bubble_sort(a)
print(a)

def insertion_sort(a):
    raise NotImplemented

a = [8, 4, 6, 9, 2, 3, 1]
insertion_sort(a)
print(a)

def shell_sort(a):
    raise NotImplemented

a = [8, 4, 6, 9, 2, 3, 1]
shell_sort(a)
print(a)