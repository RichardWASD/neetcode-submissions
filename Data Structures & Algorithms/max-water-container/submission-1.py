class Solution:
  """
  U:
      I:List of heights @ index
      O: produt
      C: Will be 2 elements
      E:Every number is the same

  I:

  """

  def maxArea(self, heights: List[int]) -> int:
    volume = 0  # Formula: minHeight_of_two_index * (r-l) -> product
    l, r = 0, len(heights) - 1
    # The short index moves if not max volume
    while l < r:
      shortest = min(heights[l], heights[r]);
      distance = r-l;
      curr_product = (distance) * shortest;

      if curr_product > volume:
        volume = curr_product;
      if(heights[l] == shortest):
        l +=1;
      else:
        r -=1;

    

    return volume
