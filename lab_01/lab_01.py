print("1)")
cnt_iter = 10
sum_ = 0

while cnt_iter > 0:
    sum_ += cnt_iter
    cnt_iter -= 1

print(f"sum = {sum_}, cnt_iter = {cnt_iter}")

sum_ = 0

for i in range (10, 0, -1):
    sum_ += i

print(f"sum = {sum_}\n")

#------------------
print("2)")
num_bin = "1011"
print(f"Binary number = {num_bin}")

enp = 0
num_dec = 0
cnt_iter = len(num_bin)

while cnt_iter > 0:
    num_dec += 2**enp * int(num_bin[cnt_iter - 1])
    enp += 1
    cnt_iter -= 1

print(f"Decimal number = {num_dec}\n")

#--------------------
print("3)")
num_bin = "1011"
print(f"Binary number = {num_bin}")

num_dec = 0
num_bin = num_bin[::-1]
cnt_iter = 0

while cnt_iter < len(num_bin):
    num_dec += 2**cnt_iter * int(num_bin[cnt_iter])
    cnt_iter += 1

print(f"Decimal number = {num_dec}\n")

#--------------------
print("4)")
num_bin = "1011"
print(f"Binary number = {num_bin}")

BIT = 3
num_bin = num_bin[::-1]
#1101
num_otc = []

cnt_bit = 0

while cnt_bit < len(num_bin):
    cnt, sum_ = 0, 0

    while cnt < BIT:
        if cnt_bit >= len(num_bin):
            break

        sum_ += 2**cnt * int(num_bin[cnt_bit])
        cnt += 1
        cnt_bit += 1

    num_otc.append(sum_)

num_otc = num_otc[::-1]
num_otc = "".join(map(str, num_otc))
print(f"Octal number = {num_otc}\n")

#-----------------------
print("5)")
num_bin = "1011"
print(f"Binary number = {num_bin}")

num_dec = 0
num_bin = list(num_bin)
cnt_iter = 0

while num_bin:
    num_dec += 2**cnt_iter * int(num_bin.pop())
    cnt_iter += 1

print(f"Decimal number = {num_dec}\n")

#-----------------------

print("6)")
num_bin = "1011"
print(f"Binary number = {num_bin}")

num_bin = list(num_bin)
BIT = 3
num_otc = []
octal = []

while num_bin:
    cnt, sum_ = 0, 0

    while cnt < BIT and num_bin:
        octal.append(int(num_bin.pop()))
        cnt += 1
    cnt = 0
    while octal:
        bin_ = octal.pop(0)
        sum_ += 2**cnt * bin_
        cnt += 1

    num_otc.append(sum_)

num_otc = "".join(map(str, num_otc[::-1]))
print(f"Octal number = {num_otc}\n")