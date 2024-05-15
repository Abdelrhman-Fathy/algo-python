
class Solution:
    class Solution:
        def maxVowels(self, s: str, k: int) -> int:
            vowels = {'a', 'e', 'i', 'o', 'u'}
            # intialize
            count = 0
            for i in range(k):
                if s[i] in vowels:
                    count += 1
            gmax = count
            for i in range(k, len(s)):

                if s[i] in vowels:
                    count += 1
                if s[i - k] in vowels:
                    count -= 1
                gmax = max(gmax, count)
            return gmax

