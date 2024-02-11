class Solution(object):
    def largestGoodInteger(self, num):
        largestInt = -1
        result = ""
        for i in range(len(num)-2):
            n = num[i]
            goodInt = -1
            if (n == num[i+1] and n == num[i+2]):
                n = int(n)
                goodInt = n * 100 + n *10 + n
            
            largestInt = max(largestInt, goodInt)

        #Sanitize Output
        if largestInt == 0:
            result = "000"
        elif largestInt != -1:
            result = str(largestInt) 

        return result