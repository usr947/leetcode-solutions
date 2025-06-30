l1 = [2,4,3]
l2 = [5,6,4]
result = []
carry = 0
for i in range (len(l1)):
      sum = l1[i]+l2[i]+carry
      if sum >=10:
            carry = 1
            result.append(sum-10)
      else:
           carry = 0
           result.append(sum)
if carry:
      result.append(carry)
print (result)