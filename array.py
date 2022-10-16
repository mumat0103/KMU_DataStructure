class Array:
    def __init__(self, len=10):
        self.len = len
        self.data = [0] * len

    def __str__(self):
        return f"{self.data}"
    
    def __len__(self):
        return len(self.data)
    
    def __setitem__(self, id, elem):
        self.data[id] = elem
        
    def __getitem__(self, id):
        return self.data[id]

if __name__ == "__main__":
    # Array객체 instance 를 하나 생성한다
    # 기본크기는 10 개이다
    arr = Array(5)

    for i in range(len(arr)):
        arr[i] = i
   
    print(arr)
    index = 3
    print(f"arr [{index}] = {arr[index]}")
    
    for i in arr:
        print(id(i), i)
        
    print(sum(arr))