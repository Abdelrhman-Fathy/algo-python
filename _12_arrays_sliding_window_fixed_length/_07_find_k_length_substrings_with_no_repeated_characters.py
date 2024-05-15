#https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/description/

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        count = 0
        #Intialize
        exist = {}
        if k > len(s):
            return count
        for i in range(k):
            if s[i] in exist:
                exist[s[i]] += 1
            else:
                exist[s[i]] = 1

        if len(exist) == k:
            count += 1

        for i in range(k, len(s)):
            if s[i] in exist:
                exist[s[i]] += 1
            else:
                exist[s[i]] = 1

            exist[s[i-k]] -= 1
            if exist[s[i-k]] == 0:
                del exist[s[i-k]]
            if len(exist) == k:
                count +=1
        return count




def test():
    sol = Solution()
    S = "havefunonleetcode"; K = 5
    #Output: 6
    result = sol.numKLenSubstrNoRepeats(S, K)
    print(result)

    S = "home"; K = 5
    #Output: 0
    result = sol.numKLenSubstrNoRepeats(S, K)
    print(result)



