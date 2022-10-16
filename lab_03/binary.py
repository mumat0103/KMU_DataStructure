class Binary:
    def __init__(self, data):
        str_ = ""
        for i in data:
            str_ += str(i)
        self.data = str_
        
    def __str__(self):
        return f"{self.data}"
    
    def __len__(self):
        return len(self.data)
    
    def __add__(self, other):
        if not isinstance(other, Binary):
            raise Exception()
        
        enp = 0
        num_dec_0 = 0
        num_dec_1 = 0
        #2진수->10진수 변환
        cnt_iter = len(self.data)
        while cnt_iter > 0:
            num_dec_0 += 2**enp * int(self.data[cnt_iter - 1])
            enp += 1
            cnt_iter -= 1
            
        enp = 0    
        cnt_iter = len(other.data)
        while cnt_iter > 0:
            num_dec_1 += 2**enp * int(other.data[cnt_iter - 1])
            enp += 1
            cnt_iter -= 1
        #10진수 덧셈            
        sum_ = num_dec_0 + num_dec_1
        #10진수->2진수 변환
        num_bin = ""
        while sum_ >= 2:    
            sum_, r = sum_ // 2, sum_ % 2
            num_bin = str(r) + num_bin
            
        num_bin = str(sum_) + num_bin
        
        return Binary(num_bin)
    
    def __getitem__(self, id):
        return self.data[id]
                
    
*data , = "110101011"
*data , = map(int, data)
b1 = Binary(data)
print(b1) #110101011
print(len(b1)) # 9
    
*data , = "110111"
*data , = map(int, data)
b2 = Binary(data)
print(b2) # 110111
print(len (b2)) # 6

b= b1 + b2
print(b) #111100010
print(len(b)) # 9
print(b[4]) # 0