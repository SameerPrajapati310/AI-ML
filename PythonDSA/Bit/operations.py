class Operations:
    def int_to_binary(self,x):
        result = ""
        while x > 0:
            if x%2 == 1:
                result += "1"
            else:
                result += "0"
            x = x//2
        return result[::-1]
    def binary_to_int(self,s):
        p = 1
        num  = 0
        s = s[::-1]
        for i in range(len(s)):
            x = int(s[i])
            if x == 1:
                num = num + p
            p = p*2
        return num
    

ans = Operations()
print(ans.int_to_binary(13))
print(ans.binary_to_int("1101"))