### Bubble Sorting Algorithm

def sort(nums):
  
  for i in range(0,len(nums)):
      for j in range(0,len(nums)-1):
          if nums[j] > nums[j+1] :
              nums[j],nums[j+1]=nums[j+1],nums[j]
          else:
              continue
  print(nums)
        
        
        
c=[0,3,4,2,1,5,7,6,9,8,13,14,11,12,-1,300,299,3]

sort(c)
