import math

BASE = 2
num_dec = 11

print(f"Decimal number = {num_dec}")

num_bin = ""

num_dec, r = num_dec // BASE, num_dec % BASE
num_bin = str(r) + num_bin

num_dec, r = num_dec // BASE, num_dec % BASE
num_bin = str(r) + num_bin

num_dec, r = num_dec // BASE, num_dec % BASE
num_bin = str(r) + num_bin

num_bin = str(num_dec) + num_bin

print(f"1) Binary number = {num_bin}\n")

#------------------------------------------------------

num_dec = 54
num_bin = ""

cnt_iter = int(math.log(num_dec, 2))

while cnt_iter > 0:    
    num_dec, r = num_dec // BASE, num_dec % BASE
    num_bin = str(r) + num_bin
    cnt_iter -= 1
    
num_bin = str(num_dec) + num_bin

print(f"2) Binary number = {num_bin}\n")

#------------------------------------------------------
num_dec = 13
num_bin = ""


while num_dec >= BASE:    
    num_dec, r = num_dec // BASE, num_dec % BASE
    num_bin = str(r) + num_bin
    
num_bin = str(num_dec) + num_bin

print(f"3) Binary number = {num_bin}\n")

#------------------------------------------------------

num = 5923
cnt_iter = int(math.log(num, 10))
sum_ = 0

while cnt_iter >= 0:
    num, r = num % (10**cnt_iter), num // (10**cnt_iter)
    sum_ += int(r)
    
    cnt_iter -= 1
    
print(f"4) sum = {sum_}\n")

#------------------------------------------------------

num = 5923
sum_ = 0

while num > 0:
    num, r = num // 10, num % 10
    sum_ += r
    
print(f"5) sum = {sum_}\n")

#------------------------------------------------------

def solution(lst):
    freq = [0] * 256
    for i in lst:
        freq[i] += 1
            
    ref = [i for i in range(len(freq)) if freq[i] == max(freq)]
    if len(lst) == len(ref):
        return[]
            
    return ref

print(solution([1, 2, 3, 4, 5, 5])) #[5]