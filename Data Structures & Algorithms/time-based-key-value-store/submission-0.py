class TimeMap:

    def __init__(self):
        self.TM = {} # key = string , val = [list of [val,timestamp]] ; CREATED HASHMAP

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.TM):
            self.TM[key] = []
        self.TM[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.TM.get(key,[]) # 
        l,r = 0, len(values) -1 

        while l <= r: 
            m = (l+r) // 2 
            if(values[m][1] <= timestamp): # 
                res = values[m][0]
                l = m + 1
            else: 
                r = m -1
        return res 