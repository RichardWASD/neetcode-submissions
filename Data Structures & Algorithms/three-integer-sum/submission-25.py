class Solution:
  """
  U:
      I: list of ints
      O: list of list(triples)
      C: No Dupe triples
      E:
  """

  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort(); # sort so we dont have to linearly search this list (kinda like binary search)
    res = [];
    nums_length = len(nums);

    for i in range(nums_length):
      l,r = i+1, nums_length-1;
      

      while(l < r):
        currSum = (nums[i]+ nums[l] + nums[r]);
        currTrip = [nums[i],nums[l],nums[r]];

        if(currSum == 0 and currTrip not in res):
          res.append([nums[i],nums[l],nums[r]]);
          l+=1;
        elif (currSum < 0):
          l+=1;
        else:
          r-=1;

    return res;
        