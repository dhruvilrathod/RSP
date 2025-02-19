def countPalindromicSubsequences(s):
        """
        :type s: str
        :rtype: int
        """
        dp = set()

        def dfs(ss):
            # print("Looking for subsequence: ", ss, "in dp: ", ss in dp)
            if ss == "":
                return
            if not ss in dp:
                if ss == ss[::-1]:
                    dp.add(ss)
            n = len(ss)
            for i in range(0,n):
                # print("checking subsequence: ", ss[:i] + ss[i+1:])
                dfs(ss[:i] + ss[i+1:])

        dfs(s)
        # print(dp)
        return len(dp) % ((10 ** 9) + 7)

print(countPalindromicSubsequences("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"))