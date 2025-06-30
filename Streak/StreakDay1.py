nums = [1,3,2,2,5,2,3,7]
res = []
for i in range (len(nums)):
      temp = []
      for j in range (len(nums)):
            if abs(nums[i]-nums[j]) == 1:
                  temp.append(nums[j])
      if temp :
            temp.append(nums[i])
            if max(temp)-min(temp)==1:
                  res.append(temp)
print (res)