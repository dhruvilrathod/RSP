class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        def subsequence(text, subseq_length):
            if subseq_length <= 0:
                return []

            if subseq_length == 1:
                return list(text)

            text_length = len(text)
            res = []
            tail_length = subseq_length - 1
            for i in range(0, text_length - tail_length):
                for tail in subsequence(text[i+1:], tail_length):
                    ans1 = text[i] + tail
                    res.append(ans1)
            return res



        def encode(text):
            enc = ""
            tmp = 1
            n = len(text)
            for i in range(n):
                if i < n-1 and text[i] == text[i+1]:
                    tmp += 1
                else:
                    enc += text[i]
                    if tmp > 1:
                        enc += str(tmp)
                        tmp = 1
            return enc

        res = subsequence(s, len(s)-k)
        res = set(res)
        enc = [encode(r) for r in res]
        ans = float('inf')
        for r in enc:
            if len(r) < ans:
                ans = len(r)
        return ans




print(Solution().getLengthOfOptimalCompression("aabbaa", 2))