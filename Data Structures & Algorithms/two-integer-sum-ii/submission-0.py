class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i= 0
        while(i < len(numbers) - 1):
            need = target - numbers[i]
            j = i +1 
            while (j < len(numbers)):
                if(numbers[j] == need):
                    return [i +1 ,j + 1]
                j +=1 
            i +=1
        return [-1,-1] 

