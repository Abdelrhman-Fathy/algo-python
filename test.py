def permutationsUnique(nums):
    result = []

    def helper(s, i, slate):
        #base case
        if i == len(s):
            result.append(slate[:])
        #recursive case
        seen = set()
        for pick in range(i, len(s)):
            if s[pick] in seen:
                continue
            seen.add(s[pick])

            s[i], s[pick] = s[pick], s[seen]
            slate.append(s[i])
            slate.append(s[i])
            slate.pop()
            s[i], s[pick] = s[pick], s[i]

    helper(nums, 0, [])
    return result