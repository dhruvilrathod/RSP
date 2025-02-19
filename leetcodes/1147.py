def longestDecomposition(text):
        """
        :type text: str
        :rtype: int
        """
        n = len(text)
        l = 0
        r = n-1

        ll = l

        ans = 0

        count = 0

        while l < r:

            print(l ,r, text[ll:l+1], text[r-count: r+1])

            if text[l] != text[r]:
                l+=1
                count += 1
            elif text[ll:l+1] != text[r-count: r+1]:
                l+=1
                count += 1                 
            else:
                print("found")
                ans += 2
                l+=1
                ll = l
                r -= (count+1)
                count = 0

        if l == r:
            ans += 1
        
        return ans


text = "antaprezatepzapreanta"
print(longestDecomposition(text))