#Fixed size window
#Find subarray of size k which have maximum sum.
class FixedSize:
    def fixedsize(self,arr,k):
        window_sum = 0
        ans = -1
        for i in range(len(arr)):
            window_sum += arr[i]
            if i >= k:
                window_sum -= arr[i-k]
            if i > k-1:
                ans = max(ans,window_sum)
        return ans

# Find lenght maximum subarray whose sum is less then equql to k
class VariableSize:
    def variablesize(self,arr,k):
        window_sum = 0
        l = 0
        ans = -1
        for i in range(len(arr)):
            window_sum += arr[i]
            while window_sum > k:
                window_sum -= arr[l]
                l+=1
            ans = max(ans,i-l+1)
        return ans

# Lenght of the longest substring without repeating character
class FrequencyMap:
    def frequencymap(self,s):
        freq = {}
        j = 0
        ans = -1
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i],0) + 1
            while freq[s[i]] > 1:
                freq[s[j]] -= 1
                if freq[s[j]] == 0:
                    del freq[s[j]]
                j+=1
            ans = max(ans,i-j+1)
        return ans

# Longest Subarray containing at most k distinct elements
class AtMostK:
    def atmostk(self,arr,k):
        m = {}
        i = 0
        ans = -1
        for j in range(len(arr)):
            m[arr[j]] = m.get(arr[j],0) + 1
            while len(m) > k:
                m[arr[i]] -= 1
                if m[arr[i]] == 0:
                    del m[arr[i]]
                i+=1
            ans = max(ans,j-i+1)
        return ans

# subarray which have exaclty k different integers:
class ExactlyK:
    def exactlyk(self,arr,k):
        freq = {}
        i = 0
        ans = 0
        for j in range(len(arr)):
            freq[arr[j]] = freq.get(arr[j],0) + 1
            while len(freq) > k:
                freq[arr[i]] -= 1
                if freq[arr[i]] == 0:
                    del freq[arr[i]]
                i+=1
            ans += j-i+1
        return ans

#s1 is permutation of s2?
class TwoFrequencyMap_Anagram:
    def twofrequency(self, s1, s2):
        one = {}

        for i in range(len(s1)):
            one[s1[i]] = one.get(s1[i], 0) + 1

        two = {}
        i = 0
        k = len(s1)

        for j in range(len(s2)):
            two[s2[j]] = two.get(s2[j], 0) + 1

            while j - i + 1 > k:
                two[s2[i]] -= 1
                if two[s2[i]] == 0:
                    del two[s2[i]]
                i += 1

            if j - i + 1 == k:
                if one == two:
                    return True

        return False


arr = [1,2,4,21,1,2,2,3]    
ans = ExactlyK()
print(ans.exactlyk(arr,3)-ans.exactlyk(arr,2))
