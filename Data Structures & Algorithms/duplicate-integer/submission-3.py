class Solution:
  '''
    U: Search the list for 2 elements that are the same
        I: list of ints
        O: Bool
        C: Num can can neg or positives
        E: empty list
  I: Brute force would be to check each index with the rest of list -> O(n^2)

  '''
  def hasDuplicate(self, nums: List[int]) -> bool:
    if(not nums):
        return False;
    book = set();
    for i in range(len(nums)):
        if(nums[i] in book):
            return True;
        else:
            book.add(nums[i]);
    return False
